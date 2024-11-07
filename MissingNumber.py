#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    arr_count = Counter(arr)
    brr_count = Counter(brr)
    
    num = []
    
    for x in brr_count:
        if brr_count[x] > arr_count.get(x, 0):
            num.append(x)
            
    for y in arr_count:
        if arr_count[y] > brr_count.get(y, 0):
            num.append(y)
    return sorted(set(num))