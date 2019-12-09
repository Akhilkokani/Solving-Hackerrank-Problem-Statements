# Problem Statement Link: https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    freq_counter = {}

    for i in arr:
        freq_counter[i] = arr.count(i)

    highest_freq_value = max ( freq_counter.values() )
    highest_freq_indexes = []

    for i in range ( max(freq_counter.keys()) ):
        if i in freq_counter and freq_counter[i] == highest_freq_value:
            highest_freq_indexes.append(i)

    return min(highest_freq_indexes)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
