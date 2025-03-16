# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

import os
from .common   import *
from .h_files  import *
from .h_util   import *
    
def check_migrations():
    try:
        
        if 0 == exec_process('python manage.py makemigrations --check --dry-run'):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def exec_migration():
    try:
        
        if 0 == exec_process('python manage.py makemigrations'):
            if 0 == exec_process('python manage.py migrate'):
                return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def create_admin():
    try:
        
        if 0 == exec_process('python manage.py createsuperuser '):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1
        
def exec_project_start(aPort=8000):
    try:
        
        if 0 == exec_process('python manage.py runserver ' + str(aPort) ):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def exec_project_shell():
    try:
        
        if 0 == exec_process('python manage.py shell'):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def exec_format_code( aFilePath ):
    try:
        
        if 0 == exec_process('black ' + aFilePath ):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1
