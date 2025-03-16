# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

from .common   import *
from .h_files  import *
from .h_util   import *

def env_check( ):
    
    # Use project prefix 
    FILE_DJ_ENV = os.path.join( DIR_ROOT, FILE_DJ_ENV_s )

    # Check app exists
    if not file_exists( FILE_DJ_ENV ):
        content = '# GENERATED' + '\n'
        file_create(FILE_DJ_ENV, content)

    return 

def env_list( ):

    # Use project prefix 
    FILE_DJ_ENV = os.path.join( DIR_ROOT, FILE_DJ_ENV_s )

    env_check( )

    # Check app exists 
    env = file_load( FILE_DJ_ENV, True )

    # Check app exists
    if not env:
        print('ERR: ' + FILE_DJ_ENV+ ' not found')
        return None   

    print( '> ENVIRONMENT:' )
    for line in env:
        if '#' not in line:
            print( '   |-- ' + line )

def env_add( aEnvVar, aValue):

    # Use project prefix 
    FILE_DJ_ENV = os.path.join( DIR_ROOT, FILE_DJ_ENV_s )

    env_check( )

    # Check app exists 
    env = file_load( FILE_DJ_ENV, True )

    # Check app exists
    if not env:
        print('ERR: ' + FILE_DJ_ENV+ ' not found')
        return None   

    found = False  

    aValue_c = aValue
    if aValue_c.lower() == 'random':
        aValue = h_random()    

    env_p = []
    for line in env:

        # module laready there, update version
        if (aEnvVar +'=') in line:
            found = True 
            line = aEnvVar + '=' + aValue

        env_p.append( line )

    if not found: 
        aEnvVar += '=' + aValue

        env_p.append( aEnvVar )

    file_write( FILE_DJ_ENV, env_p)

def env_delete( aEnvVar ):

    # Use project prefix 
    FILE_DJ_ENV = os.path.join( DIR_ROOT, FILE_DJ_ENV_s )

    # Check app exists 
    env = file_load( FILE_DJ_ENV, True )

    # Check app exists
    if not env:
        return   

    env_p = []
    for line in env:

        # module laready there, update version
        if not (aEnvVar +'=') in line:
            env_p.append( line )

    file_write( FILE_DJ_ENV, env_p)

def env_comment( aEnvVar ):

    # Use project prefix 
    FILE_DJ_ENV = os.path.join( DIR_ROOT, FILE_DJ_ENV_s )

    # Check app exists 
    env = file_load( FILE_DJ_ENV, True )

    # Check app exists
    if not env:
        return   

    found = False  

    env_p = []
    for line in env:

        # module laready there, update version
        if line.startswith( aEnvVar + '='):
            found = True 
            line = '#' + line

        env_p.append( line )

    file_write( FILE_DJ_ENV, env_p)

def env_uncomment( aEnvVar ):

    # Use project prefix 
    FILE_DJ_ENV = os.path.join( DIR_ROOT, FILE_DJ_ENV_s )
    
    # Check app exists 
    env = file_load( FILE_DJ_ENV, True )

    # Check app exists
    if not env:
        return   

    found = False  

    env_p = []
    for line in env:

        # module laready there, update version
        if line.startswith( '#' + aEnvVar + '='):
            found = True 
            line = line[1:]

        env_p.append( line )

    file_write( FILE_DJ_ENV, env_p)
