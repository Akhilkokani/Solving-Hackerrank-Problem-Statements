# Problem Statement Link:https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    prev_cloud = 0
    flag = False
    for i in range( len(c) ):
        curr_cloud = (prev_cloud+k)%n
        if flag == True: 
            break
        else:
            print (prev_cloud, "->", curr_cloud)
            if c[curr_cloud] == 1:
                e -= 3
            else:
                e -= 1
        if curr_cloud == 0: 
            flag = True
        prev_cloud = curr_cloud
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
