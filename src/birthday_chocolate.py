# Problem Statement Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    s_len = len(s)

    if m == 1:
        for i in s:
            if i == d:
                count += 1

    elif m >= 2:
            for i in range ( s_len ):
                sub = []
                k = 0

                j = s[i]
                no_of_times_to_iterate = m - 1
                p = i + 1

                sub.append ( s[i] )

                while k < no_of_times_to_iterate:

                    if p != i and p < s_len:
                        sub.append ( s[p] )

                    p += 1
                    k += 1

                if sum(sub) == d and len(sub) == m:
                    count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
