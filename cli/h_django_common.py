# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

from .common   import *
from .h_files  import *
from .h_util   import *

def cfg_load( FILE_PATH=FILE_DJ_SETTINGS_s ):

    retcode = COMMON.OK
    content = []

    try:
        
        raw_content = file_load( FILE_PATH, True ) # as list

        if not raw_content:
            print ('Err loading ['+FILE_PATH+'] file')
            return COMMON.NOT_FOUND, None 

        # print('Content: ' + raw_content)    
        content = raw_content

    except Exception as e:

        print('Err loading ['+FILE_PATH+']: ' + str(e) )
        retcode = COMMON.ERR

    return retcode, content

def cfg_save( FILE_PATH, aContent ):

    retcode = COMMON.OK

    try:
        
        file_content = ''
        
        if type( aContent ) is list:
            for line in aContent:
                file_content += line + '\n'

        # expect a string here        
        else:
            file_content = aContent

        file_write( FILE_PATH, file_content)

    except Exception as e:

        retcode = COMMON.ERR

    return retcode

def cfg_format( FILE_PATH ):

    retcode = COMMON.OK

    try:    

        if not ( file_exists( FILE_PATH ) ):
            print( 'Err locate ['+FILE_PATH+']' )
            return COMMON.ERR

        # Apply 'Black' formatter over the file
        result = exec_process( 'black ' + FILE_PATH )

        #if COMMON.OK != result:
        #    print('Err formating settings')
        #    exit(1)   

    except Exception as e:

        print('Err formating exeption: ' + str(e) )
        retcode = COMMON.ERR

    return retcode

def file_format( FILE_PATH ):
    
    return cfg_format( FILE_PATH )

def file_process( FILE_PATH, MARKER, aContent ):

    retcode, content = cfg_load( FILE_PATH )

    file_c = []

    MARKER_BEGIN = '#'    + MARKER
    MARKER_END   = '#END' + MARKER
    processing   = False 

    for line in content:

        if MARKER_BEGIN in line: 
            
            processing   = True

            content_new   = ''
            content_new += MARKER_BEGIN + '\n'
            content_new += aContent     + '\n'
            content_new += MARKER_END   + '\n'

            file_c.append( content_new )

        elif processing:

            if MARKER_END in line:
                processing   = False

        else:
            file_c.append( line )  

    return cfg_save( FILE_PATH, file_c )

def h_var_typology( content ):
    
    if not content:
        return COMMON.CFG_VAR_NA

    if '=' in content and '[' in content:
        return COMMON.CFG_VAR_LIST    

    if '=' in content and '{' in content:
        return COMMON.CFG_VAR_DICT  

    if '=' in content and not '[' in content and not '}' in content:
        return COMMON.CFG_VAR_SIMPLE

    # Default is unknown
    return COMMON.CFG_VAR_NA        

def h_extract_sections( content ):

    file_imports  = []
    file_sections = []

    for line in content:

        # import here    
        if 'from ' in line or 'import ' in line:
            file_imports.append ( h_del_lsep( line ) ) # strip line separators

        # main sections here
        if '=' in line:
            file_sections.append( line.split('=')[0].strip() )

    print("Imports  : " + str( file_imports  ) )       
    print("Sections : " + str( file_sections ) ) 

    return file_sections

def cfg_imports( FILE_PATH ):

    retcode = COMMON.OK
    imports = []

    retcode, content = cfg_load( FILE_PATH )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] file')
        return retcode, None

    for line in content:

        # import here    
        if 'from ' in line or 'import ' in line:
            imports.append ( h_del_lsep( line ) ) # strip line separators

    return retcode, imports

def cfg_sections( FILE_PATH ):

    retcode  = COMMON.OK
    sections = []

    retcode, content = cfg_load( FILE_PATH )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] file')
        return retcode, None

    for line in content:

        # import here    
        if '=' in line and '#' not in line:
            sections.append( line.split('=')[0].strip() )

    return retcode, sections

def cfg_var_upd( FILE_PATH, var_name, var_value, SkipQuotes=False):

    retcode = COMMON.NOT_FOUND

    retcode, content = cfg_load( FILE_PATH )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] file')
        return retcode

    new_content = []
    found = False
    for line in content:

        if var_name not in line:

            new_content.append( line )
            continue

        found = True

        # variable found
        retcode = COMMON.OK 

        var_typology = h_var_typology( line )

        if COMMON.CFG_VAR_SIMPLE == var_typology:
            
            aValue_c = var_value
            if aValue_c.lower() == 'random':
                var_value = h_random()  

            if SkipQuotes:
                line = var_name + ' = ' + var_value
            else:    
                line = var_name + ' = ' + '"' + var_value + '"'
            
            new_content.append( line )

    if not found:
        line = var_name + ' = ' + '"' + var_value + '"'
        new_content.append( line + '\n' )

    # Variable was found and successfully processed
    if COMMON.OK == retcode:
        cfg_save( FILE_PATH, new_content )

    return retcode

def cfg_var_comment( FILE_PATH, var_name):

    retcode = COMMON.NOT_FOUND

    retcode, content = cfg_load( FILE_PATH )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] file')
        return retcode

    new_content = []
    found = False
    for line in content:

        if var_name not in line:

            new_content.append( line )
            continue

        found = True

        # variable found
        retcode = COMMON.OK 

        var_typology = h_var_typology( line )

        if COMMON.CFG_VAR_SIMPLE == var_typology:
            
            line = '#' + line 
            
            new_content.append( line + '\n' )

    if not found:
        line = var_name + ' = ' + '"' + var_value + '"'
        new_content.append( line + '\n' )
        
    # Variable was found and successfully processed
    if COMMON.OK == retcode:
        cfg_save( new_content )

    return retcode

def cfg_var_print( FILE_PATH, var_name ):

    retcode = COMMON.NOT_FOUND

    retcode, content = cfg_load( FILE_PATH )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] file')
        return retcode

    new_content = []
    for line in content:

        if var_name not in line:

            new_content.append( line )
            continue
        
        else: 

            # variable found
            retcode = COMMON.OK 

            var_typology = h_var_typology( line )

            print(' > Var found    : ' + h_del_lsep( line )        )
            print(' > Var typology : ' + commonTxt( var_typology ) )

    if COMMON.OK != retcode:
         print(' > Var not found ')

    return retcode    

def cfg_section_get( FILE_PATH, section ):

    retcode = COMMON.NOT_FOUND

    retcode, content = cfg_load( FILE_PATH )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] file')
        return retcode

    section_content = []
    section_begin   = False 
    section_end     = False 
    retcode         = COMMON.NOT_FOUND

    # This is used to count [, {
    section_control_begin = '' 
    section_control_end   = '' 
    section_control_idx   = 0 

    for line in content:

        line = h_del_lsep( line )

        # We have an end here
        if section_end:
            break 

        # Computing is over
        if section_begin and section_control_idx == 0:
            section_end = True 
            retcode     = COMMON.OK
            continue 

        # Computing is active 
        if section_begin:

            section_content.append( line )

            if section_control_begin in line:
                section_control_idx += 1    

            if section_control_end in line:
                section_control_idx -= 1    

        # Other things
        if not section_begin and section not in line:
            continue 

        # Here is a match
        if '=' in line: 
            section_begin = True

        # Detect topology 
        var_typology = h_var_typology( line )

        # Simple, one-time 
        if COMMON.CFG_VAR_SIMPLE == var_typology:
            
            section_content.append( line )

            section_end = True 
            retcode     = COMMON.OK

        # Lists (we can have mixed types)
        if COMMON.CFG_VAR_LIST == var_typology:

            # save the first line            
            section_content.append( line )

            section_begin = True 

            retcode = COMMON.OK

            section_control_begin = '['
            section_control_end   = ']'
            section_control_idx   = 1 

        # Dicts (we can have mixed types)
        if COMMON.CFG_VAR_DICT == var_typology:

            # save the first line            
            section_content.append( line )

            section_begin = True 

            retcode = COMMON.OK

            section_control_begin = '{'
            section_control_end   = '}'
            section_control_idx   = 1 

    # Exit
    if COMMON.OK == retcode:
        #print( 'BEGIN >>>' )
        #line_nb = 0
        #for item in section_content:
        #    line_nb += 1
        #    print ( str(line_nb) + '|'+ item )  
        #print( '<<< END' )
        pass         
    else:    
        print( ' > Section ['+section+'] not found ' )

    # Exit point 
    return retcode, section_content

def cfg_section_update( FILE_PATH, aSectionName, aSectionContent ):

    retcode = COMMON.OK

    retcode, content = cfg_load( FILE_PATH ) # as list 

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] file')
        return retcode

    content_p = []

    section_start = False 
    section_end   = False 

    for line in content:

        if line.startswith( aSectionName ):
            
            section_start = True 
            content_p.append(aSectionContent)
            continue 

        if not section_start:

            content_p.append( line )

        if section_start and not section_end and (']' == line):

            section_end = True 
            continue

        if section_end:

            content_p.append( line )

    # Exit
    if COMMON.OK == retcode:

        # Save the content
        cfg_save(FILE_PATH, content_p )
        cfg_format( FILE_PATH )

    # Exit point 
    return retcode

def cfg_section_list( FILE_PATH, SECTION_NAME ):

    retcode = COMMON.OK

    # load INSTALLED_APPS
    retcode, content = cfg_section_get(FILE_PATH, SECTION_NAME)

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] -> ['+SECTION_NAME+'] section')
        return retcode, None

    return retcode, content[1:(len(content)-1)] # slice, cut first & last element

def cfg_section_add_item( FILE_PATH, SECTION_NAME, aItem, SkipQuotes=False ):

    # Check for duplicates
    retcode, all_items = cfg_section_list( FILE_PATH, SECTION_NAME)

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] -> ['+SECTION_NAME+']')
        return retcode, None

    retcode, section_content = cfg_section_get( FILE_PATH, SECTION_NAME )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] -> ['+SECTION_NAME+']')
        return retcode, None

    # Processing (LIST) type 
    section_content_str = '' 
    
    for line in section_content:
        
        # insert new app at the end
        if ']' in line:
            if SkipQuotes:
                section_content_str += '    ' + aItem + ',\n'
            else:    
                section_content_str += '    "' + aItem + '",\n'

        section_content_str += line + '\n'
    
    retcode = cfg_section_update( FILE_PATH, SECTION_NAME, section_content_str)

    # Exit
    if COMMON.OK == retcode:
        print( 'Section ['+SECTION_NAME+'] updated successfully' )
    else:
        print( 'Error updating ['+SECTION_NAME+'] section' )

    # Exit point 
    return retcode, section_content

def cfg_section_add_item_first( FILE_PATH, SECTION_NAME, aItem ):

    # Check for duplicates
    retcode, all_items = cfg_section_list( FILE_PATH, SECTION_NAME)

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] -> ['+SECTION_NAME+']')
        return retcode, None

    retcode, section_content = cfg_section_get( FILE_PATH, SECTION_NAME )

    if COMMON.OK != retcode:

        print('Err loading ['+FILE_PATH+'] -> ['+SECTION_NAME+']')
        return retcode, None

    # Processing (LIST) type 
    section_content_str = '' 

    is_first_line = False    
    for line in section_content:
        
        # insert new app at the end
        if '[' in line:
            is_first_line = True
            section_content_str += line + '\n' 
            continue

        if is_first_line:
            is_first_line = False
            section_content_str += '    "' + aItem + '",\n'

        # All other lines
        section_content_str += line + '\n'
    
    retcode = cfg_section_update( FILE_PATH, SECTION_NAME, section_content_str)

    # Exit
    if COMMON.OK == retcode:
        print( 'Section ['+SECTION_NAME+'] updated successfully' )
    else:
        print( 'Error updating ['+SECTION_NAME+'] section' )

    # Exit point 
    return retcode, section_content
