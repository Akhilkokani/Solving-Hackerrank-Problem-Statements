# Problem Statement Link: https://www.hackerrank.com/challenges/halloween-sale/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    if p > s: return 0
    hmg = 1
    ms = cog = p
    while True:
        if (cog-d) <= m: cog = m
        else: cog -= d

        if (ms+cog) > s: break

        hmg += 1
        ms += cog

    return hmg
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
