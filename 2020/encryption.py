# Problem Statement Link: https://www.hackerrank.com/challenges/encryption/problem

#!|bin|python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    c = math.ceil( math.sqrt(len(s)) )
    us = [ [] ] * c

    for i in range( len(us) ):
        us[i] = s[:c]
        s = s[c:]

    for j in range( len(max(us, key=len)) ):
        for i in range( len(us) ):
            s += us[i][:1]
            us[i] = us[i][1:]
        s += " "
    
    return s
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
