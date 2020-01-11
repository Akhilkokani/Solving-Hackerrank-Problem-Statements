# Problem Statement Link: https://www.hackerrank.com/challenges/the-time-in-words/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    niw = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
    'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    
    if m == 0:
        return ( niw[h-1] + " o' clock" )

    elif m > 20 and m < 30:
        return ( "twenty " + niw[ int(str(m)[1])-1 ] + " minutes past " + niw[h-1] )
    
    elif m == 30: 
        return ( "half past " + niw[h-1] )
    
    elif m == 45:
        return ( "quarter to " + niw[h] )

    elif m <= 20:
        if m is 15: return ( "quarter past " + niw[ h-1 ] )
        else: 
            if h == 1:
                return ( niw[m-1] + " minute past " + niw[h-1] )
            else:
                return ( niw[m-1] + " minutes past " + niw[h-1] )
    
    else:
        rm = 60 - m
        if rm <= 20: 
            return ( niw[rm-1] + " minutes to " + niw[h] )
        else:
            return ( "twenty " + niw[ int(str(rm)[1])-1 ] + " minutes to " + niw[h] )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
