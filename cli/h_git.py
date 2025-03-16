# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

import os
from .common   import *
from .h_files  import *
from .h_util   import *
    
def git_changes():
    try:
        
        if 0 == exec_process('git diff --name-only'):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def git_log():
    try:
        
        if 0 == exec_process('git log --oneline --graph --all'):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1
    
def git_commit():
    try:

        git_comment = input(' Add Comment: ')
        
        # add dummy if not provided
        if not git_comment or '' == git_comment:
            git_comment = ''

        if 0 == exec_process( f"git commit -am \"{git_comment}\"" ):
            if 0 == exec_process( 'git push' ):
                return True
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1
        
def git_tag():
    try:
        
        git_tag     = input(' TAG Name: ')
        git_comment = input(' TAG Comment: ')

        if 0 == exec_process( f"git tag -a {git_tag} -m '{git_comment}'" ):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def git_list_tags():
    try:
        
        if 0 == exec_process('git describe --tags --abbrev=0'):
            return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1

def git_revert():
    try:
        
        confirm = input('DANGER: This command reverts the latest commit. Confirm y/N: ')
        if 'y' != confirm.strip().lower():
            # nothing is done
            return False    

        if 0 == exec_process('git reset --hard HEAD~1'):
            if 0 == exec_process('git push origin HEAD --force'):
                return True 
        
        return False

    except Exception as e:
        print(' > ERR: ' + str(e) )
        return -1
