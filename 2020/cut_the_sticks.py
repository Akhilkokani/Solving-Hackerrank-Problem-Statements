# Problem Statement Link: https://www.hackerrank.com/challenges/cut-the-sticks/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    sticks_out = []
    for a in range( len(arr) ) :
        if len(arr) >= 1:
            sticks_out.append( len(arr) )
            smallest = min(arr)
            while (arr.count(smallest)):
                arr.remove(smallest)
            arr = [x - smallest for x in arr]
    return sticks_out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
