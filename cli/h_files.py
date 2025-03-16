# -*- encoding: utf-8 -*-
"""
Copyright (c) AppSeed.us
"""

import os, fnmatch, shutil, json

from .common   import *
from .h_util   import *

def dir_create(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception as e:
        raise e

def dir_exists ( aPath ):
    return os.path.isdir( aPath )   

def dir_rm ( aPath ):
    if os.path.exists( aPath ):
        shutil.rmtree( aPath )          

def file_exists( aPath ):

    try:

        if open( aPath, 'r'):
            return True

    except:
        return False  

def file_save( aPath, aContent ):

    with open(aPath, 'w') as f:

        if isinstance(aContent, str):
            f.write( aContent )
            return True

        if isinstance(aContent, list): 
            content_str = ''    
            for line in aContent:
                content_str += line + '\n'       

            f.write( content_str )
            return True

        if isinstance(aContent, dict): 

            content_str = ''    
            for key, value in aContent.items():
                content_str += key + '=' + value + '\n'       

            f.write( content_str )
            return True

    return False

def file_append( aPath, aNewContent ):

    with open(aPath, "r") as file:

       content  = file.read()
       content += '\n' + aNewContent

       return file_save( aPath, content )

    return False

def file_load( path, as_list=False ):

    try:

        f = open( path, 'r')
        if f:

            if as_list:
                content = f.read().splitlines()
            else:
                content = f.read()    
            
            f.close()
            return content

    except UnicodeDecodeError as err:

        print(" *** UnicodeDecodeError: {0}".format(err))
        return None

    except Exception as e:

        print (' *** Err loading file: ' + str( e ) )
        return None     

# Dummy wrapper 
def file_content( aFilePath, aMark=None ):
    return file_load( aFilePath, aMark )

def file_rm ( aPath ):
    if file_exists( aPath ):
        os.remove( aPath )

def list_files( aPath, aExcludePath, aExt=None ):

    matches = []

    for root, dirnames, filenames in os.walk( aPath ):

        # Exclude DIRs like ENV, migrations .. etc
        if any(ext in root for ext in aExcludePath):
            continue

        if aExt: 

            for filename in fnmatch.filter(filenames, '*.' + aExt ):

                item = os.path.join(root, filename)

                matches.append( item )
        else:

            for filename in filenames:

                item = os.path.join(root, filename)

                matches.append( item )

    return matches

def file_write( path, content, f_append=False ): 

    try:

        f = None

        if file_exists( path ):
            if f_append:    
                f = open( path, 'a+')
            else:
                f = open( path, 'w+')    
        else:
            f = open( path, 'w+')

        if not f:
            print( 'Error open file ' )
            return False

        if type(content) is list:
            content_p = ''
            for line in content:
                content_p += line + '\n'

            content = content_p

        f.seek(0) 
        f.write( content )
        f.truncate()

        f.close()
        return True

    except Exception as e:

        print( 'ERR file_write(): ' + str( e ) )
        return False

    except:

        print ( ' *** Err processing file ' + str(path) )
        return False
    
def file_create( path, content='' ):

    return file_write( path, content )

def json_load( aPath ):

    if file_exists( aPath ):
        return json.loads( file_load( aPath ) ) 

    return None
