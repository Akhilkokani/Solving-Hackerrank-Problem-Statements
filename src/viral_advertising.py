# Problem Statement Link: https://www.hackerrank.com/challenges/strange-advertising/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    shared = 5
    cumulative = 0

    for i in range( int(input()) ):
        liked = int(shared/2)
        cumulative += liked
        shared = liked * 3

    fptr.write(str(cumulative) + '\n')

    fptr.close()
