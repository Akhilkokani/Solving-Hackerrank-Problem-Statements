# Problem Statement Link: https://www.hackerrank.com/challenges/equality-in-a-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    max_freq_ele = max( set(arr), key=arr.count )
    return len(arr) - arr.count(max_freq_ele)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
