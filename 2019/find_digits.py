# Problem Statement Link: https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):

        n = int(input())
        digits = list( map(int, str(n)) )
        count = 0

        for i in digits:
            if i != 0 and n%i == 0:     # Logic
                count += 1

        fptr.write(str(count) + '\n')

    fptr.close()
