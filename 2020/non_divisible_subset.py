# Problem Statement Link: https://www.hackerrank.com/challenges/non-divisible-subset

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    ss = []
    results = []
    for i in s:
        results.append( (i%k) )
    for i in range( len(results) ):
        a = results[i]
        for j in range(i+1, len(results)):
            b = results[j]
            if (a + b) == k:
                c = max( results.count(a), results.count(b) )
                ss.append(c)
            else:
                if a not in ss:
                    ss.append(a)
                if b not in ss:
                    ss.append(b)
    return len(ss)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])
    k = 13
    # s = list(map(int, input().rstrip().split()))
    # s = [770528134, 663501748, 384261537, 800309024, 103668401, 538539662, 385488901, 101262949, 557792122, 46058493]
    s = [ 2375782, 21836421, 2139842193, 2138723, 23816, 21836219, 2948784, 43864923, 283648327, 23874673]
    result = nonDivisibleSubset(k, s)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
