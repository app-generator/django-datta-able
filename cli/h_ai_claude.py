# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

import random, string, json, statistics, re, pprint, time
from datetime import datetime

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

from django.conf import settings
from django.http import JsonResponse

from .common        import *
from .h_util        import *
from .h_code_parser import *
from .h_django      import *

def model_suggest_charts(aModelClassImport, aDebug=False):

    start_time = time.time()

    retVal = COMMON.ERR
        
    model_class = name_to_class( aModelClassImport )

    if not model_class:
        print( f" > ERR getting class for model [{aModelClassImport}]" )
        return retVal, None, None, None
    
    retVal, csv_content = h_model_to_csv( aModelClassImport )

    if COMMON.OK != retVal:
        print( f" > ERR getting CSV Representation for model [{aModelClassImport}]" )
        return retVal, None, None, None

    csv_header = csv_content[0]
    csv_content.pop()

    aQuestion  = f"I need to extract charts from a CSV with the following fields: {csv_header}."
    aQuestion += "Here are the first lines from the file."

    idx = 0
    for l in csv_content:

        idx += 1
        if idx > 5:
            break 
        
        aQuestion += l + '\n'

    aQuestion += '\nBased on the above information and field data, please suggest all relevant charts and context information in JSON format with folowing sections:'
    aQuestion += '\nNode Summary: with a title about the data provided in the CSV and a description with full input.'
    aQuestion += '\nAnoter node "potential_uses" where are suggestions regarding the reports we can get from the input.'
    aQuestion += '\nSuggested charts node will present a list of chart types with a short explanation and the relevant fields correlated with the x-axis, y-axis.'
    aQuestion += '\nHere is the expected response that should be a valid JSON without extra text fields in response (helps response extraction and processing):'
    aQuestion += '\n{'
    aQuestion += '\n    "summary":{'
    aQuestion += '\n        "title":"CONTENT_HERE",'
    aQuestion += '\n        "description":"CONTENT_HERE",'
    aQuestion += '\n    "},'
    aQuestion += '\n    "potential_uses":['
    aQuestion += '\n        "FIRST use explanation",'
    aQuestion += '\n        "And the next ones",'
    aQuestion += '\n    "],'    
    aQuestion += '\n    "suggested_charts":['
    aQuestion += '\n        {},'
    aQuestion += '\n        {},'
    aQuestion += '\n    "],' 
    aQuestion += '\n}'

    if aDebug:
        print('>>>>>>>>>>>>>>>>>>>>>>>>')
        print( aQuestion ) 
        print('<<<<<<<<<<<<<<<<<<<<<<<<') 

    message = f"{HUMAN_PROMPT}{aQuestion}\n\n{AI_PROMPT}"

    client = Anthropic(api_key=getattr(settings, 'ANTHROPIC_API_KEY'))

    response            = None 
    response_title      = None 
    response_json       = None
    response_conclusion = None 
    response_data       = None 

    try:
    
        response = client.completions.create(
            model="claude-2.1",
            prompt=message,
            max_tokens_to_sample=1000,
        )

        response            = response.completion.split('```')
        response_title      = response[0]
        response_json       = response[1].replace('json', '')
        response_conclusion = response[2]
        response_data       = json.loads(response_json)

        retVal = COMMON.OK 

    except json.JSONDecodeError:
        print(f"> ERR: {str(e)}")
        retVal = COMMON.ERR
    except Exception as e:
        print(f"> ERR: {str(e)}")
        retVal = COMMON.ERR

    print("--- %s seconds ---" % (time.time() - start_time))
    return retVal, response_title, response_conclusion, response_data

'''
aCvsFile needs to be in `media` folder
'''
def csv_suggest_charts(aCvsFile, aDebug=False):

    start_time = time.time()

    retVal = COMMON.ERR
        
    csv_content = file_load( os.path.join('media', aCvsFile), True )

    if not csv_content:
        print( f" > Input file [{aCvsFile}], not found in the MEDIA folder" )
        return retVal, None, None, None
    
    csv_header = csv_content[0] 
    csv_content.pop()

    aQuestion  = f"I need to extract charts from a CSV with the following fields: {csv_header}."
    aQuestion += "Here are the first lines from the file."

    idx = 0
    for l in csv_content:

        idx += 1
        if idx > 5:
            break 
        
        aQuestion += l + '\n'

    aQuestion += '\nBased on the above information and field data, please suggest all relevant charts and context information in JSON format with folowing sections:'
    aQuestion += '\nNode Summary: with a title about the data provided in the CSV and a description with full input.'
    aQuestion += '\nAnoter node "potential_uses" where are suggestions regarding the reports we can get from the input.'
    aQuestion += '\nSuggested charts node will present a list of chart types with a short explanation and the relevant fields correlated with the x-axis, y-axis.'
    aQuestion += '\nHere is the expected response that should be a valid JSON without extra text fields in response (helps response extraction and processing):'
    aQuestion += '\n{'
    aQuestion += '\n    "summary":{'
    aQuestion += '\n        "title":"CONTENT_HERE",'
    aQuestion += '\n        "description":"CONTENT_HERE",'
    aQuestion += '\n    "},'
    aQuestion += '\n    "potential_uses":['
    aQuestion += '\n        "FIRST use explanation",'
    aQuestion += '\n        "And the next ones",'
    aQuestion += '\n    "],'    
    aQuestion += '\n    "suggested_charts":['
    aQuestion += '\n        {},'
    aQuestion += '\n        {},'
    aQuestion += '\n    "],' 
    aQuestion += '\n}'

    if aDebug:
        print('>>>>>>>>>>>>>>>>>>>>>>>>')
        print( aQuestion ) 
        print('<<<<<<<<<<<<<<<<<<<<<<<<') 

    message = f"{HUMAN_PROMPT}{aQuestion}\n\n{AI_PROMPT}"

    client = Anthropic(api_key=getattr(settings, 'ANTHROPIC_API_KEY'))

    response            = None 
    response_title      = None 
    response_json       = None
    response_conclusion = None 
    response_data       = None 

    try:
    
        response = client.completions.create(
            model="claude-2.1",
            prompt=message,
            max_tokens_to_sample=1000,
        )

        response            = response.completion.split('```')
        response_title      = response[0]
        response_json       = response[1].replace('json', '')
        response_conclusion = response[2]
        response_data       = json.loads(response_json)

        retVal = COMMON.OK 

    except json.JSONDecodeError:
        print(f"> ERR: {str(e)}")
        retVal = COMMON.ERR
    except Exception as e:
        print(f"> ERR: {str(e)}")
        retVal = COMMON.ERR

    print("--- %s seconds ---" % (time.time() - start_time))
    return retVal, response_title, response_conclusion, response_data

'''
aCvsFile needs to be in `media` folder
'''
def csv_query(aCvsFile, aDataQuery, aRowLimit=10, aDebug=False):

    start_time = time.time()

    retVal = COMMON.ERR
        
    csv_content = file_load( os.path.join('media', aCvsFile), True )

    if not csv_content:
        print( f" > Input file [{aCvsFile}], not found in the MEDIA folder" )
        return retVal, None, None, None
    
    csv_header = csv_content[0] 
    csv_content.pop()

    aQuestion  = f"{aDataQuery,} from this CSV file with the following fields: {csv_header}."
    aQuestion += "Here is the content."

    idx = 0
    for l in csv_content:

        idx += 1
        if idx > aRowLimit:
            break 
        
        aQuestion += l + '\n'
 
    aQuestion += '\n}'

    if aDebug:
        print('>>>>>>>>>>>>>>>>>>>>>>>>')
        print( aQuestion ) 
        print('<<<<<<<<<<<<<<<<<<<<<<<<') 

    message = f"{HUMAN_PROMPT}{aQuestion}\n\n{AI_PROMPT}"

    client = Anthropic(api_key=getattr(settings, 'ANTHROPIC_API_KEY'))

    response = None 

    try:
    
        response = client.completions.create(
            model="claude-2.1",
            prompt=message,
            max_tokens_to_sample=1000,
        )

        response = response.completion
        retVal = COMMON.OK 

    except Exception as e:
        print(f"> ERR: {str(e)}")
        retVal = COMMON.ERR

    print("--- %s seconds ---" % (time.time() - start_time))
    return retVal, response

