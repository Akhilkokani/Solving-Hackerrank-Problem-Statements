# Problem Statement Link: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

#!/bin/python3

import math
import os
import random
import re
import sys
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        m = []
        rowsum = [0]*n
        colsum = [0]*n

        for _ in range(n):
            m.append(list(map(int, input().rstrip().split())))

            rowsum[ _ ] = sum(m[-1])    # Logic Start
            colsum = list(map(lambda a, b: a+b, colsum, m[-1]))
        
        rowsum.sort()
        colsum.sort()
        
        if rowsum == colsum:
            fptr.write("Possible" + '\n')
        else:
            fptr.write("Impossible" + '\n')     # Logic End

    fptr.close()
