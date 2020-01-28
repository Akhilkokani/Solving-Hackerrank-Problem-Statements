# Problem Statement Link: https://www.hackerrank.com/challenges/lisa-workbook/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, K, T):
    cnt = 0 # special problems
    i = 0   # chapter number
    j = 1   # page number
    m = 1   # problem number

    while i < n:
        if m <= j and j <= min(m + K - 1, T[i]): cnt += 1
        j += 1
        m += K
        if m > T[i]: # next chapter
            i += 1
            m = 1

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
