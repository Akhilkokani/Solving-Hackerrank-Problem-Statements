# Problem Statement link: https://www.hackerrank.com/challenges/apple-and-orange/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    sam_house_range = range(s, t+1)
    apples_fallen_near_house = 0
    oranges_fallen_near_house = 0

    for i in range(0, len(apples)):
        if s <= (a + apples[i]) <= t:
            apples_fallen_near_house += 1

    for i in range(0, len(oranges)):
        if s <= (b + oranges[i]) <= t:
            oranges_fallen_near_house += 1

    print(apples_fallen_near_house)
    print(oranges_fallen_near_house)

if __name__ == '__main__':

    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
