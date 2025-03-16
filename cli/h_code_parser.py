# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

import os, ast, astor, importlib

from .common   import *
from .h_files  import *
from .h_util   import *

def name_to_class(name: str):

    try:
        # Process the path 
        cls_name    = name.split('.')[-1]             # Extract Class Name
        cls_import  = name.replace('.'+cls_name, '')  # Extract Import path

        module = importlib.import_module(cls_import)  # Here is expected a valid package 

        # If all good, a class is returned 
        return getattr(module, cls_name)               
    except:

        # Nothing found, bozzo input
        return None 
    
def h_model_to_csv(aModelClassImport, aNbrRows=COMMON.ROWS_MAX):

    retVal  = COMMON.ERR
    dataset = []
    header  = []

    aModelClass = name_to_class( aModelClassImport ) 

    if not aModelClass:
        print( f" > ERR getting class for model [{aModelClassImport}]" )
        return retVal, None 

    for f in aModelClass._meta.fields:
        header.append( f.name ) 

    dataset.append( h_list_to_str(header) )

    idx = 0
    for row in aModelClass.objects.all():
        
        idx += 1
        if idx > aNbrRows:
            break 
        
        dataset_row = []

        for f in header:
            data = getattr(row, f)

            if not data:
                dataset_row.append('')
                continue

            data = str( data )

            if COMMON.CSV_SEP in data:

                dataset_row.append( f"\"{data}\"" )
            
            else:

                dataset_row.append( data ) 
        
        dataset.append( h_list_to_str( dataset_row ) )

    return COMMON.OK, dataset

class PythonFileClassManipulator:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r') as file:
            self.source_code = file.read()
        self.tree = ast.parse(self.source_code)

    def get_class_names(self):
        return [node.name for node in ast.walk(self.tree) if isinstance(node, ast.ClassDef)]

    def extract_class_code(self, class_name):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                # Get the source code lines
                source_lines = self.source_code.splitlines()
                
                # Find the start and end lines of the class
                start_line = node.lineno - 1  # ast line numbers are 1-indexed
                end_line = self._find_class_end(node, source_lines)
                
                # Extract and return the class code
                class_code = '\n'.join(source_lines[start_line:end_line])
                return class_code
        
        print(f"Class '{class_name}' not found in the file.")
        return None 
    
    def _find_class_end(self, class_node, source_lines):
        # Find the last line of the class definition
        end_line = class_node.lineno
        indent = self._get_indent(source_lines[end_line - 1])
        
        for line_num in range(end_line, len(source_lines)):
            if line_num >= len(source_lines):
                return line_num
            line = source_lines[line_num]
            if line.strip() and self._get_indent(line) <= indent:
                return line_num
        
        return len(source_lines)

    def _get_indent(self, line):
        return len(line) - len(line.lstrip())

    def replace_class(self, class_name, new_class_code):
        new_class_ast = ast.parse(new_class_code).body[0]
        
        for i, node in enumerate(self.tree.body):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                self.tree.body[i] = new_class_ast
                break
        else:
            raise ValueError(f"Class '{class_name}' not found in the file.")

    def save_modified_file(self, output_path=None):
        modified_code = astor.to_source(self.tree)
        output_path = output_path or self.file_path
        with open(output_path, 'w') as file:
            file.write(modified_code)

def add_field_to_class(class_code, new_field_name, new_field_value):
    # Parse the class code into an AST
    tree = ast.parse(class_code)

    # Find the class definition
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Create a new AST node for the field
            new_field = ast.Assign(
                targets=[ast.Name(id=new_field_name, ctx=ast.Store())],
                value=ast.Constant(value=new_field_value)
            )
            
            # Add the new field to the class body
            node.body.append(new_field)

    # Convert the modified AST back to source code
    modified_code = astor.to_source(tree)
    return modified_code

def create_field_node(field_name, field_type, **kwargs):
    if field_type != DbField.FK_FIELD:
        raise ValueError("This function is specifically for adding ForeignKey fields.")

    related_model = kwargs.pop('related_model', None)
    if not related_model:
        raise ValueError("'related_model' is required for ForeignKey fields.")

    on_delete = kwargs.pop('on_delete', None)
    if not on_delete:
        raise ValueError("'on_delete' is required for ForeignKey fields.")

    return ast.Assign(
        targets=[ast.Name(id=field_name, ctx=ast.Store())],
        value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='models', ctx=ast.Load()),
                attr='ForeignKey',
                ctx=ast.Load()
            ),
            args=[ast.Name(id=related_model, ctx=ast.Load())],
            keywords=[
                ast.keyword(
                    arg='on_delete',
                    value=ast.Attribute(
                        value=ast.Name(id='models', ctx=ast.Load()),
                        attr=on_delete.split('.')[-1],
                        ctx=ast.Load()
                    )
                ),
                *[ast.keyword(arg=key, value=ast.Str(s=value) if isinstance(value, str) else ast.Constant(value=value))
                  for key, value in kwargs.items()]
            ]
        )
    )

def add_fk_to_django_model(model_code, field_name, field_type, position=None, **kwargs):
    # Parse the model code into an AST
    tree = ast.parse(model_code)

    # Find the class definition
    class_def = next((node for node in tree.body if isinstance(node, ast.ClassDef)), None)
    if not class_def:
        raise ValueError("No class definition found in the provided code.")

    # Create the new field node
    new_field = create_field_node(field_name, field_type, **kwargs)

    # Add the new field to the class body
    if position is None or position >= len(class_def.body):
        class_def.body.append(new_field)
    else:
        class_def.body.insert(position, new_field)

    # Convert the modified AST back to source code
    modified_code = astor.to_source(tree)
    return modified_code

def add_field_to_django_model(model_code, field_name, field_type, position=None, **kwargs):
    tree = ast.parse(model_code)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Create the new field
            field_args = [ast.keyword(arg=key, value=ast.Constant(value=value)) for key, value in kwargs.items()]
            new_field = ast.Assign(
                targets=[ast.Name(id=field_name, ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id=field_type, ctx=ast.Load()),
                    args=[],
                    keywords=field_args
                )
            )
            
            # Add the new field to the class body
            if position is None or position >= len(node.body):
                node.body.append(new_field)
            else:
                node.body.insert(position, new_field)
    
    # Convert the modified AST back to source code
    modified_code = astor.to_source(tree)
    return modified_code

def remove_field_from_django_model(model_code, field_name):

    # Parse the model code into an AST
    tree = ast.parse(model_code)

    # Find the class definition
    class_def = next((node for node in tree.body if isinstance(node, ast.ClassDef)), None)
    if not class_def:
        raise ValueError("No class definition found in the provided code.")

    # Remove the field from the class body
    class_def.body = [node for node in class_def.body if not (isinstance(node, ast.Assign) and 
                                                              isinstance(node.targets[0], ast.Name) and 
                                                              node.targets[0].id == field_name)]

    # Convert the modified AST back to source code
    modified_code = astor.to_source(tree)
    return modified_code

def manipulate_python_file(file_path, class_to_replace, new_class_code):
    manipulator = PythonFileClassManipulator(file_path)
    
    print("Classes found in the file:")
    class_names = manipulator.get_class_names()
    for name in class_names:
        print(f"- {name}")

    if class_to_replace in class_names:
        manipulator.replace_class(class_to_replace, new_class_code)
        manipulator.save_modified_file()
        print(f"\nClass '{class_to_replace}' has been replaced and the file has been updated.")
    else:
        print(f"\nClass '{class_to_replace}' not found in the file.")

