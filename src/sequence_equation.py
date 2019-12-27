# Problem Statement Link: https://www.hackerrank.com/challenges/permutation-equation/problem

#!/bin/python3

import math
import os
import random
import re
import sys
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    for x in range(min(p), max(p)+1):
        fptr.write( str(p.index( p.index(x)+1 )+1) + '\n' ) # Logic
    
    fptr.write('\n')

    fptr.close()
