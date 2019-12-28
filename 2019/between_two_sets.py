# Problem Statement Link: https://www.hackerrank.com/challenges/between-two-sets/problem

#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a_len = len(a)
    b_len = len(b)

    i = 0
    int_considered = 1
    count = 0

    while i < 1000:
        credible = 0

        for k in a:
            if (int_considered%k) == 0:
                credible += 1

        for k in b:
            if (k%int_considered) == 0:
                credible += 1

        if credible == (a_len + b_len):
            count += 1

        i += 1
        int_considered += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
