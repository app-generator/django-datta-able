# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

from .common           import *
from .h_files          import *
from .h_util           import *
from .h_django_common  import *

def urls_load( ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )

    return cfg_load( FILE_DJ_URLS )

def urls_imports( ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )

    return cfg_imports( FILE_DJ_URLS )

def urls_sections( ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )

    return cfg_sections( FILE_DJ_URLS )

def urls_save( content ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )

    return cfg_save( FILE_DJ_URLS, content )

def urls_format( ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )

    return cfg_format( FILE_DJ_URLS ) 

def urls_section_get( ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )

    return cfg_section_get( FILE_DJ_URLS, 'urlpatterns' )

def urls_list( ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )

    return cfg_section_list( FILE_DJ_URLS, 'urlpatterns' )

def urls_add_rule( aNewValue ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( DIR_ROOT, FILE_DJ_URLS_s )
    
    return cfg_section_add_item( FILE_DJ_URLS, 'urlpatterns', aNewValue, True )
