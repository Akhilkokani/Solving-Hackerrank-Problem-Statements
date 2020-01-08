# Problem Statement Link: https://www.hackerrank.com/challenges/minimum-distances/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    mini = []
    for i in range( len(a) ):
        if a[i] in a[i+1:]:
            mini.append( a[i+1:].index(a[i]) + i+1 - a.index(a[i]) )

    if len(mini) >= 1:
        return min( mini )
        
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
