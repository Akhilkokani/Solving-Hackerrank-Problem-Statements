# Problem Statement Link: https://www.hackerrank.com/challenges/picking-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    sub_a = [ [] ] * len(a)
    
    for i in range(0, len(a)):
        temp = []
        for j in range(0, len(a)):
            if i != j and abs( a[i] - a[j] ) <= 1:
                m = n = True
                if len(temp) >= 1:
                    for k in temp:
                        if abs( a[i] - k ) > 1:
                            m = False
                        if abs( a[j] - k ) > 1:
                            n = False
                if m == True and temp.count( a[i] ) != a.count( a[i] ): # Not adding same number twice
                    temp.append( a[i] )
                if n == True and temp.count( a[j] ) != a.count( a[j] ): # Not adding same number twice
                    temp.append( a[j] )
        sub_a[i] = temp
    return max( [len(x) for x in sub_a] )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
