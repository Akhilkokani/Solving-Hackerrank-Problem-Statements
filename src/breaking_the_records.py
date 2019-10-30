#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    num_of_times_highest_score_increased = 0
    num_of_times_lowest_score_increased = 0

    previous_highest_score = scores[0]
    previous_lowest_score = scores[0]

    for i in scores:
        if i > previous_highest_score:
            previous_highest_score = i
            num_of_times_highest_score_increased += 1

        elif i < previous_lowest_score:
            previous_lowest_score = i
            num_of_times_lowest_score_increased += 1

    return [num_of_times_highest_score_increased, num_of_times_lowest_score_increased]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
