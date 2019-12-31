# Problem Statement Link: https://www.hackerrank.com/challenges/append-and-delete/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    flag = False
    con = True if len(s) < len(t) else False

    for i in range( max(len(s), len(t)) ):
        if con:
            if (len(t) - len(s)) % 2 != 0:
                return "No"
            else:
                return "Yes"
        else:
            try:
                if s[i] != t[i] or flag == True:
                    k -= 2 # 1 for delete operation and another 1 for append operation
                    flag = True
            except IndexError:
                k -= 1
                pass
            
    if k >= 0 or s == t:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
