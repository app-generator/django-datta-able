# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

from .common           import *
from .h_files          import *
from .h_util           import *
from .h_django_common  import *

def settings_load( ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_load( FILE_DJ_SETTINGS )

def settings_imports( ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_imports( FILE_DJ_SETTINGS )

def settings_sections( ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_sections( FILE_DJ_SETTINGS )

def settings_var_upd( aVarName, aVarValue):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_var_upd( FILE_DJ_SETTINGS, aVarName, aVarValue )

def settings_var_upd_bool( aVarName, aVarValue):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_var_upd( FILE_DJ_SETTINGS, aVarName, aVarValue, True )

def settings_var_print( aVarName ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_var_print( FILE_DJ_SETTINGS, aVarName )

def settings_section_get( aSectionName ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( FILE_DJ_SETTINGS_s )

    return cfg_section_get( FILE_DJ_SETTINGS, aSectionName )

def settings_section_update( aSectionName, aSectionContent ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_section_update( FILE_DJ_SETTINGS, aSectionName, aSectionContent)

def settings_apps_list( ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )

    return cfg_section_list( FILE_DJ_SETTINGS, 'INSTALLED_APPS')

def settings_apps_add( aNewApp, aPos=COMMON.POS_END ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )
    
    if COMMON.POS_END == aPos:
        cfg_section_add_item( FILE_DJ_SETTINGS, 'INSTALLED_APPS', aNewApp )
    else: 
        cfg_section_add_item_first( FILE_DJ_SETTINGS, 'INSTALLED_APPS', aNewApp )

def settings_middleware_add( aNewApp, aPos=COMMON.POS_END ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( DIR_ROOT, FILE_DJ_SETTINGS_s )
    
    if COMMON.POS_END == aPos:
        cfg_section_add_item( FILE_DJ_SETTINGS, 'MIDDLEWARE', aNewApp )
    else: 
        cfg_section_add_item_first( FILE_DJ_SETTINGS, 'MIDDLEWARE', aNewApp )

def settings_dyn_get(aSectionName):

    ret, cfg_dyn_l = settings_section_get( aSectionName )
    
    if COMMON.OK != ret:
        print(' > ERR getting section: ' + aSectionName )
        return ret, None 

    # here we store the values 
    rules = {}

    # cut head, tail 
    rules_l = cfg_dyn_l[1:len(cfg_dyn_l)-1]

    for line in rules_l:
        key = line.split(':')[0].replace("'", '').replace('"', '').replace(',', '').replace(' ', '')
        val = line.split(':')[1].replace("'", '').replace('"', '').replace(',', '').replace(' ', '')
        rules[key] = val
    
    return COMMON.OK, rules 

def settings_dyn_set(aSectionName, aDict):

    aDictContent = aSectionName + ' = {' + os.linesep
    for k in aDict.keys():
        aDictContent += COMMON.TAB + f"'{k}' : '{aDict[k]}'," + os.linesep

    aDictContent += '}'

    return settings_section_update( aSectionName, aDictContent )

def settings_dyn_add(aSectionName, aKey, aVal):

    ret, aDict = settings_dyn_get(aSectionName)
    if COMMON.OK != ret:
        return ret, None
    
    aDict[aKey] = aVal

    pp( aDict )
    
    return settings_dyn_set(aSectionName, aDict)

def settings_dyn_del(aSectionName, aKey):

    ret, aDict = settings_dyn_get(aSectionName)
    if COMMON.OK != ret:
        return None 
    
    if aKey in aDict:
        del aDict[ aKey ]
    
    return settings_dyn_set(aSectionName, aDict)
