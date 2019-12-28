# Problem Statement Link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful_days = 0
    for a in range(i, j+1):
        num_reversed = int ( str(a)[::-1] ) # Converting int to string and reversing it and again converting it to int
        if (a - num_reversed)%k == 0:
            beautiful_days += 1
    return beautiful_days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
