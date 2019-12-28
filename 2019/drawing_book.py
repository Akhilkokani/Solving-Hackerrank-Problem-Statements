# Problem Statement Link: https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    pages_to_turn = [0, 0]
    rev_num = n

    for i in range( 1, n+1 ):
        if i < p and (i % 2) != 0:
                pages_to_turn[0] += 1
        if rev_num > p and (rev_num % 2) == 0:
                pages_to_turn[1] += 1
        rev_num -= 1

    return min( pages_to_turn )
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
