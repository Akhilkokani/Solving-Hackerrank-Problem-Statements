# Problem Statement Link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    divisible_sum_pairs_count = 0

    if k == 1:
        for i in ar:
            if i == k:
                divisible_sum_pairs_count += 1
    elif k >= 2:
        for i in range ( n ):
                sub = [0,0]
                j = 0

                no_of_times_to_iterate = n - 1
                p = i + 1

                sub[0] = ar[i]

                while j < no_of_times_to_iterate:

                    if p != i and p < n:
                        sub[1] = ar[p]
                    
                    if p < n and (sub[0]+sub[1])%k == 0:
                        divisible_sum_pairs_count += 1

                    p += 1
                    j += 1
    return divisible_sum_pairs_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
