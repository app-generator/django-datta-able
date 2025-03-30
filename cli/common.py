# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

import os, subprocess
from pprint import pp 

# DJANGO Globals
DJANGO_APPS           = None  

# Globals 
DIR_ROOT              = '.' # points to the root 
DIR_TMPL              = os.path.join( DIR_ROOT, 'templates' )
DIR_STATIC            = os.path.join( DIR_ROOT, 'static'    )

DIR_DJ_CONFIG         = 'config'
DIR_DJ_APP_DEFAULT    = 'home'

FILE_DJ_MANAGE_s      = 'manage.py'
FILE_DJ_ENV_s         = '.env'
FILE_DJ_DEPS_s        = 'requirements.txt'
FILE_DJ_URLS_s        = os.path.join( DIR_DJ_CONFIG      , 'urls.py'     )
FILE_DJ_SETTINGS_s    = os.path.join( DIR_DJ_CONFIG      , 'settings.py' )
FILE_DJ_INIT_s        = os.path.join( DIR_DJ_CONFIG      , '__init__.py' )
FILE_DJ_MODELS_s      = os.path.join( DIR_DJ_APP_DEFAULT , 'models.py'   )

FILE_CI_BUILD_s       = 'build.sh'
FILE_CI_RENDER_s      = 'render.yaml'
FILE_DOCKER_s         = 'Dockerfile'
FILE_README_s         = 'README.md' 

class COMMON:

    NULL              = None # not set
    NA                = -1   # not set
    OK                =  0   # All good   (unix style)
    ERR               =  1   # Err bumped (unix style)
    NOT_FOUND         =  2   # file or directory not found
    INPUT_ERR         =  3   # file or directory not found
    PROCESSED         =  4

    POS_FIRST         = 'FIRST'
    POS_END           = 'END'
    
    CHART_VERBS       = ['sum', 'count', 'avg', 'min', 'max']
    CHART_VERB_SUM    = 'sum'
    CHART_VERB_COUNT  = 'count'
    CHART_VERB_AVG    = 'avg'
    CHART_VERB_MIN    = 'min'
    CHART_VERB_MAX    = 'max'

    ROWS_MAX          = 9999
    CSV_SEP           = ','

    # Settings vars typologies 
    CFG_VAR_NA        = 10 # Type is undetected
    CFG_VAR_SIMPLE    = 11 # Ex: SECRET_KEY
    CFG_VAR_LIST      = 12 # Ex: INSTALLED_APPS, MIDDLEWARE
    CFG_VAR_DICT      = 13 # List of Dicts, Ex: AUTH_PASSWORD_VALIDATORS 

    TAB                = '    '
    TAB2               = TAB  + TAB
    TAB3               = TAB2 + TAB

    TYPE_STRING        = 'string'
    TYPE_STRING_DJ     = 'models.CharField'

    TYPE_TEXT          = 'text'
    TYPE_TEXT_DJ       = 'models.TextField'

    TYPE_INT           = 'int'
    TYPE_INT_DJ        = 'models.IntegerField'    

    TYPE_INTEGER       = 'integer'
    TYPE_INTINTEGER_DJ = 'models.IntegerField'    

    TYPE_NUMBER        = 'number'
    TYPE_NUMBER_DJ     = 'models.IntegerField'    

    TYPE_FLOAT         = 'float'
    TYPE_FLOAT_DJ      = 'models.FloatField'    

    TYPE_DATE          = 'date'
    TYPE_DATE_DJ       = 'models.DateTimeField'    

    TYPE_TIME          = 'date'
    TYPE_TIME_DJ       = 'models.DateTimeField'    

# Recover errors for COMMON class
def errInfo( aErrorCode ):

    if COMMON.NA         == aErrorCode: return 'Not Set'
    if COMMON.ERR        == aErrorCode: return 'Error Generic'
    if COMMON.OK         == aErrorCode: return 'OK'
    if COMMON.NOT_FOUND  == aErrorCode: return 'Not Found'
    if COMMON.INPUT_ERR  == aErrorCode: return 'Input error'

    return str( aErrorCode )

def commonTxt( aCode ):

    if COMMON.CFG_VAR_NA     == aCode: return 'CFG Var unknown typology'
    if COMMON.CFG_VAR_SIMPLE == aCode: return 'CFG Var SIMPLE'
    if COMMON.CFG_VAR_LIST   == aCode: return 'CFG Var LIST'
    if COMMON.CFG_VAR_MIXED  == aCode: return 'CFG Var MIXT (list of dicts)'

    return str( aCode )

class DbField:
    CHAR_FIELD    = "models.CharField"
    TEXT_FIELD    = "models.TextField"
    INTEGER_FIELD = "models.IntegerField"
    BOOLEAN_FIELD = "models.BooleanField"
    DATE_FIELD    = "models.DateTimeField"
    FLOAT_FIELD   = "models.FloatField"
    BOOL_FIELD    = "models.BooleanField"
    FK_FIELD      = "models.ForeignKey"
    NA            = None

def str_to_db_type( aStr ):
    if not aStr:
        return None 
    
    # input normalization
    aStr = aStr.lower().replace(' ', '')

    if 'int'     == aStr: return DbField.INTEGER_FIELD
    if 'integer' == aStr: return DbField.INTEGER_FIELD
    if 'num'     == aStr: return DbField.INTEGER_FIELD
    if 'number'  == aStr: return DbField.INTEGER_FIELD

    if 'str'     == aStr: return DbField.CHAR_FIELD
    if 'string'  == aStr: return DbField.CHAR_FIELD

    if 'text'    == aStr: return DbField.TEXT_FIELD

    if 'float'   == aStr: return DbField.FLOAT_FIELD

    if 'date'    == aStr: return DbField.DATE_FIELD
    if 'time'    == aStr: return DbField.DATE_FIELD

    if 'bool'    == aStr: return DbField.BOOL_FIELD

    return DbField.NA

# Pandas to Django Type Mapping
django_fields = {
    'int'           : 'models.IntegerField(blank=True, null=True)',
    'integer'       : 'models.IntegerField(blank=True, null=True)',
    'string'        : "models.TextField(blank=True, null=True)",
    'string_unique' : "models.TextField(blank=True, null=False, unique=True)",
    'object'        : "models.TextField(blank=True, null=True)",
    'object_unique' : "models.TextField(blank=True, null=False, unique=True)",
    'int64'         : 'models.IntegerField(blank=True, null=True)',
    'float64'       : 'models.FloatField(blank=True, null=True)',
    'bool'          : 'models.BooleanField(null=True)',
}

def exec_process(aCmd):
    try:
        return os.system( aCmd )
    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def exec_subprocess( full_cmd ):

    retcode = COMMON.OK
    stdout  = ''
    stderr  = ''

    try:

        # create project in src
        result = subprocess.run( full_cmd.split(' '))

        retcode = result.check_returncode() 

    except Exception as e:

        retcode = COMMON.ERR

    return retcode

def h_del_lsep( line ):

    if line:
        line = line.replace('\n', '').replace('\r', '')

    return line    

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  

