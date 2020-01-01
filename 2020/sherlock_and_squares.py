# Problem Statement Link: https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=false

#!/bin/python3

from math import ceil, floor, sqrt
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    return floor( sqrt(b) ) - ceil( sqrt(a) ) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
