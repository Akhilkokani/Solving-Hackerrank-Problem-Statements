# Problem Statement Link: https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    counter = 1
    count = 0
    for i in range( len(s) ):
        if counter == 1 and s[i] is not 'S':
            count += 1
        
        elif counter == 2 and s[i] is not 'O':
            count += 1
        
        elif counter == 3 and s[i] is not 'S':
            count += 1

        if counter <= 2: counter += 1
        else: counter = 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
