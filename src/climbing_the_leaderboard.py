# Problem Statement Link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rankings = []
    leaderboard = sorted(set(scores), reverse = True)
    l = len(leaderboard)
    for a in alice:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        rankings.append( (l+1) )
    return rankings

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
