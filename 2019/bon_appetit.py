# Problem Statement Link: https://www.hackerrank.com/challenges/bon-appetit/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    bill.pop ( k )
    total_bill = sum ( bill )
    amount_to_be_paid_by_each_person = total_bill / 2
    overchage = b - amount_to_be_paid_by_each_person

    if overchage == 0:
        print ("Bon Appetit")
    else:
        print ( int(overchage) )

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
