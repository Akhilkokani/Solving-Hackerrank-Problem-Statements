# Problem Statement Link: https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    going_above_sea_level = 0
    coming_back_to_sea_level = 0

    going_below_sea_level = 0
    climbing_back_to_sea_level = 0

    valleys_climbed = 0

    for i in s:
        if going_above_sea_level >= 0 and going_below_sea_level == 0 and i == 'U':
            going_above_sea_level += 1

        elif going_above_sea_level > 0 and i == 'D':
            coming_back_to_sea_level += 1
            if going_above_sea_level == coming_back_to_sea_level:
                going_above_sea_level = coming_back_to_sea_level = 0

        elif going_above_sea_level == 0 and i == 'D':
            going_below_sea_level += 1
            
        elif going_below_sea_level > 0 and i == 'U':
            climbing_back_to_sea_level += 1
            if going_below_sea_level == climbing_back_to_sea_level:
                going_below_sea_level = climbing_back_to_sea_level = 0
                valleys_climbed += 1
    return valleys_climbed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
