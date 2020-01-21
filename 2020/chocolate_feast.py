# Problem Statement Link: https://www.hackerrank.com/challenges/chocolate-feast/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    ct = nwl = n//c
    while nwl > 1 and nwl >= m:
        temp = abs( (nwl%m)-nwl ) // m
        ct += temp
        nwl = temp + (nwl%m)
    return ct

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
