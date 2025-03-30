# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

import random, string, time, sys
from datetime import datetime
import django
from django.utils import timezone
from django.contrib.auth import get_user_model

from .common        import *
from .h_files       import *
from .h_util        import *
from .h_shell       import *
from .h_code_parser import *

def get_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DIR_DJ_CONFIG + ".settings")
    from collections import OrderedDict
    from django.apps import apps
    from django.conf import settings
    from django.core import management

    # Needs a single init     
    if not apps.ready:
        apps.app_configs = OrderedDict()
        apps.ready       = False
        apps.populate(settings.INSTALLED_APPS)

    return apps

def check_db_conn():
    apps = get_django()

    from django.db import connection
    from django.db.utils import OperationalError
    db_conn = None
    while not db_conn:
        try:
            connection.ensure_connection()
            db_conn = True
        except OperationalError:
            print('Database unavailable, waiting 1 second...')
            time.sleep(1)        

        print('Connecton OK')

def get_apps():
    retVal = []
    apps = get_django()
    for app in apps.get_app_configs():
        retVal.append( app.name )
    return retVal     

def get_models(aApp):

    retVal = []
    apps = get_django()
    models = apps.get_app_config( aApp ).get_models()
    for m in models:
        retVal.append( m )
    return retVal
    
def get_models_name(aApp):

    retVal = []
    models = get_models( aApp )
    for m in models:
        retVal.append( m.__name__ )
    return retVal

def get_model_by_name(aApp, aModelname):

    models = get_models( aApp )
    for m in models:
        if m.__name__ == aModelname:
            return m 
    return None

def get_model_fields(aModelClass):
    retVal = []
    for f in aModelClass._meta.fields:
        retVal.append( f )
    return retVal        

def get_model_fk(aModelClass):
    retVal = {}
    for f in aModelClass._meta.fields:
        if type( f ) is django.db.models.fields.related.ForeignKey:
            #print( ' FK: ' +  ) 
            f_class = f.related_model.__module__ + '.' + f.related_model.__name__
            retVal[ f.name ] = f_class
    return retVal        

def get_model_fk_values(aModelClass):
    retVal = {}
    for f in aModelClass._meta.fields:
        if type( f ) is django.db.models.fields.related.ForeignKey:
            f_class = f.related_model.__module__ + '.' + f.related_model.__name__
            retVal[ f.name ] = list( name_to_class( f_class ).objects.all() )
    return retVal 

# v = verbose
def get_model_fields_v(aModelClass):
    retVal = {}
    for f in aModelClass._meta.fields:
        retVal[ f.name ] = f.__class__.__name__
    return retVal 

def check_model_migration( aModelClass ):

    from django.db.utils import OperationalError
    try:
        aModelClass.objects.last()
        return True
    except OperationalError:
        return False

def extract_class_code(aFilePath, aClassName):

    file_content = file_load( aFilePath )
    if not file_content:
        print(' > ERR loading file: ' + aFilePath) 
        return None

    manipulator = PythonFileClassManipulator(aFilePath)
    return manipulator.extract_class_code(aClassName)

def add_model(aAppName, aModelName):

    target_file = os.path.join(DIR_ROOT, aAppName, 'models.py')

    if aAppName not in get_apps():
        print(' > ERR: App not registered: ' + aAppName) 
        print('     |- Expected on of: ' + str( get_apps() ) ) 
        return
    
    if aModelName in get_models_name(aAppName):
        print(' > ERR: ' + aModelName + ' already defined in ' + aAppName) 
        return
    else:
        target_file_c = file_load( target_file )
        model_class   = f"class {aModelName}(models.Model)"
        if model_class in target_file_c:
            print(' > ERR: ' + aModelName + ' already defined in ' + aAppName) 
            return
    
    model_code = file_load( os.path.join(DIR_ROOT, 'templates', 'generator', 'model.tmpl') )
    if not model_code:
        print(' > ERR loading template ') 
        return
    
    model_code = model_code.replace('__MODEL_NAME__', aModelName)
    
    file_append( target_file, model_code )
    
    # format code
    exec_format_code( target_file )

    # Check dry-run status
    exec_migration()

def add_model_field(aAppName, aModelName, aFieldName, aFieldType, **kwargs):

    file_path = os.path.join( aAppName, 'models.py' )

    # Check Input 
    if aAppName not in get_apps():
        print(' > ERR: App not registered: ' + aAppName) 
        print('     |- Expected on of: ' + str( get_apps() ) ) 
        return

    file_c = extract_class_code( file_path, aModelName )
    if not file_c:
        print(' > ERR: Model [' +aModelName+ '] not found in app: ' + aAppName) 
        return
            
    str1 = aFieldName + '='
    str2 = aFieldName + ' ='
    str3 = aFieldName + ' = '
    if str1 in file_c or str2 in file_c or str3 in file_c:
        print(' > ERR: Field [' +aFieldName+ '] already in model ' + aModelName) 
        return            

    aFieldTypeDB  = str_to_db_type( aFieldType )
    aFieldProps   = {}
    aFieldProps['blank'] = True
    aFieldProps['null'] = True
    aFieldClass = None

    if DbField.CHAR_FIELD == aFieldTypeDB:
        aFieldProps['max_length']=255

    if DbField.NA == aFieldTypeDB:

        # We can have class type
        aFieldClass = name_to_class(aFieldType)
        if not aFieldClass:
            print(' > ERR: Unsupported aFieldType [' +aFieldType+ '] ') 
            return  
        
        aFieldTypeDB = DbField.FK_FIELD

    kwargs = aFieldProps 
    
    manipulator = PythonFileClassManipulator(file_path)
    model_code = manipulator.extract_class_code(aModelName)
    model_code_upd = None 
    
    if DbField.FK_FIELD == aFieldTypeDB:
        model_code_upd = add_fk_to_django_model( model_code, field_name=aFieldName, field_type=aFieldTypeDB, related_model=aFieldClass.__name__, on_delete="models.CASCADE", position=1, **kwargs)
    else:
        model_code_upd = add_field_to_django_model( model_code, field_name=aFieldName, field_type=aFieldTypeDB, position=1, **kwargs)
    
    manipulator.replace_class(aModelName, model_code_upd )
    manipulator.save_modified_file()

    # format code
    exec_format_code( file_path )

    # Check dry-run status
    exec_migration()

def del_model_field(aAppName, aModelName, aFieldName):

    file_path = os.path.join( aAppName, 'models.py' )

    # Check Input 
    if aAppName not in get_apps():
        print(' > ERR: App not registered: ' + aAppName) 
        print('     |- Expected on of: ' + str( get_apps() ) ) 
        return

    file_c = extract_class_code( file_path, aModelName )
    if not file_c:
        print(' > ERR: Model [' +aModelName+ '] not found in app: ' + aAppName) 
        return
    
    manipulator = PythonFileClassManipulator(file_path)
    model_code = manipulator.extract_class_code(aModelName)
    model_code_upd = remove_field_from_django_model(model_code, aFieldName) 

    manipulator.replace_class(aModelName, model_code_upd )
    manipulator.save_modified_file()

    # format code
    exec_format_code( file_path )

    # Check dry-run status
    exec_migration()
    
def get_users():
    return get_user_model().objects.all()

def get_user(aInput):
    
    user = get_users().filter(username=aInput).first()
    if not user:
        user = get_users().filter(email=aInput).first()

    return user 
