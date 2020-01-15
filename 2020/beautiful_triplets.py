#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    bt = 0
    for i in arr:
        extra = 0
        if i > 0 and (abs(i-d) in arr) and (abs(i-d)-d in arr):
            if arr.count(i) > 1: extra = arr.count(i)
            if arr.count(abs(i-d)) > 1: extra += arr.count(abs(i-d))
            if arr.count(abs(i-d)-d) > 1: extra += arr.count(abs(i-d)-d)
            if extra > 0: bt += extra
            else: bt += 1
    return bt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
