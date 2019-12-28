# Problem Statement Link: https://www.hackerrank.com/challenges/utopian-tree/problem

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
        tree_height = 1
        for i in range(1, n+1):
            if i%2 == 0:
                tree_height += 1
            else:
                tree_height += tree_height
        fptr.write(str(tree_height) + '\n')

    fptr.close()
