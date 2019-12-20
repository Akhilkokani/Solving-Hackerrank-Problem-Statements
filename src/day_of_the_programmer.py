# Problem Statement Link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Lear year function
def leap_year(year):

    # For Julian calendar
    if year <= 1917:
        if year % 4 == 0:
            return True
        else:
            return False

    # For Gregorian calendar
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918" # Julian to Gregorian Switch Year
    elif year >= 1919:
        if leap_year(year):
            return "12.09." + str ( year )
        elif leap_year(year) == False:
            return "13.09." + str ( year )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
