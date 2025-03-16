# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

from .common   import *
from .h_files  import *
from .h_util   import *

def deps_list( ):
    
    # Use project prefix 
    FILE_DJ_DEPS = os.path.join( DIR_ROOT, FILE_DJ_DEPS_s )

    # Check app exists 
    requirements = file_load( FILE_DJ_DEPS, True )

    # Check app exists
    if not requirements:
        print('ERR: ' + FILE_DJ_DEPS+ ' not found')
        return None   

    print( '> Dependencies:' )
    for line in requirements:
        if '#' not in line:
            print( '   |-- ' + line )

def deps_add( aModule, aVersion=None):

    # Use project prefix 
    FILE_DJ_DEPS = os.path.join( DIR_ROOT, FILE_DJ_DEPS_s )

    # Check app exists 
    requirements = file_load( FILE_DJ_DEPS, True )

    # Check app exists
    if not requirements:
        print('ERR: ' + FILE_DJ_DEPS+ ' not found')
        return None   

    aModule = aModule.lower()
    found   = False  

    requirements_p = []
    for line in requirements:
        line = line.lower() 

        # module laready there, update version
        if aModule == line or ((aModule +'==') in line):

            found = True 
            if aVersion:
                line = aModule + '==' + aVersion
            else:    
                line = aModule

        requirements_p.append( line )

    if not found: 
        if aVersion:
            aModule += '==' + aVersion

        requirements_p.append( aModule )

    file_write( FILE_DJ_DEPS, requirements_p)

def deps_delete( aModule ):

    # Use project prefix 
    FILE_DJ_DEPS = os.path.join( DIR_ROOT, FILE_DJ_DEPS_s )
    
    # Check app exists 
    requirements = file_load( FILE_DJ_DEPS, True )

    # Check app exists
    if not requirements:
        print('ERR: ' + FILE_DJ_DEPS+ ' not found')
        return None   

    aModule = aModule.lower()

    requirements_p = []
    for line in requirements:
        line = line.lower() 

        # module laready there, update version
        if aModule == line or ((aModule +'==') in line):
            pass
        else:                
            requirements_p.append( line )

    file_write( FILE_DJ_DEPS, requirements_p)
