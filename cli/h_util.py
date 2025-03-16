# -*- encoding: utf-8 -*-
"""
Copyright (c) App-Generator.dev | AppSeed.us
"""

import random, string
from datetime import datetime

from .common import *
    
def h_random(aLen=6):
    letters = string.ascii_letters
    digits  = string.digits
    chars   = '_<>,.+'
    return ''.join(random.choices( letters + digits + chars, k=aLen))

def h_random_ascii(aLen=6):
    letters = string.ascii_letters
    digits  = string.digits
    return ''.join(random.choices( letters + digits, k=aLen))

def h_ts():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def h_list_to_str(aList, aSep=COMMON.CSV_SEP):
    return aSep.join(aList)
