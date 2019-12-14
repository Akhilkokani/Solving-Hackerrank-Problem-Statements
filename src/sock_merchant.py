# https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    distinct_values = list ( set(ar) )
    no_of_pairs = 0
    for i in distinct_values:
        if ar.count(i) % 2 == 0:
            no_of_pairs += ar.count(i)/2
        else:
            no_of_pairs += (ar.count(i) - 1)/2
    return int(no_of_pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
