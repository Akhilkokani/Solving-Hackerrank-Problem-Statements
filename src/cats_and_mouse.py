# Problem Statement Link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    dist_left_from_cat_a = abs(x-z)
    dist_left_from_cat_b = abs(y-z)

    if dist_left_from_cat_a == dist_left_from_cat_b:
        return ("Mouse C")
    elif dist_left_from_cat_a < dist_left_from_cat_b:
        return ("Cat A")
    elif dist_left_from_cat_b < dist_left_from_cat_a:
        return ("Cat B")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
