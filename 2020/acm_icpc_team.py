# Problem Statement Link: https://www.hackerrank.com/challenges/acm-icpc-team/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    max_topics = []
    for i in range( len(topic) ):        # Check all permutations... (Ex: '1011')
        for j in range( i+1, len(topic) ): # Ex: j = '0101'
            # Add both attende's values (1's & 0's).
            # Convert the resulting value to string, because, integer can't be directly converted to list in python3.
            # Convert it to list, as it's easy to count number of 1's and 2's from a list.
            a = list( str( int(topic[i]) + int(topic[j]) ) )    # a = ['1', '1', '1', '2']

            # Count number of one's and two's in list
            # No. of (two's + one's) act as max number of topics a two member team can have for this permutation.
            max_topics.append( (a.count('2') + a.count('1')) )
    
    # Maximum value of max_topics list.
    # Find the max. from max_topcs list and count how many of them exist.
    # Because they act as number of two member team's who have knowledge of max amount of topics. 
    return [ max(max_topics), max_topics.count(max(max_topics)) ]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
