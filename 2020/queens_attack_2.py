#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, o):
    mov_l = mov_r = c_q 
    mov_d = mov_u = r_q
    mov_tr = [r_q, c_q]
    mov_tl = [r_q, c_q]
    mov_br = [r_q, c_q]
    mov_bl = [r_q, c_q]
    ac = 0

    for pos in range(1, n+1):
        if (mov_u-1) >= 1 and [(mov_u-1), c_q] not in o:
            mov_u -= 1
            ac += 1

        if (mov_d+1) <= n and [(mov_d+1), c_q] not in o:
            mov_d += 1
            ac += 1

        if (mov_l-1) >= 1 and [r_q, (mov_l-1)] not in o:
            mov_l -= 1
            ac += 1

        if (mov_r+1) <= n and [r_q, (mov_r+1)] not in o:
            mov_r += 1
            ac += 1

        if (mov_tr[0]-1) >= 1 and (mov_tr[1]+1) <= n and [(mov_tr[0]-1), (mov_tr[1]+1)] not in o:
            mov_tr[0] -= 1
            mov_tr[1] += 1
            ac += 1
        
        if (mov_bl[0]+1) <= n and (mov_bl[1]-1) >= 1 and [(mov_bl[0]+1), (mov_bl[1]-1)] not in o:
            mov_bl[0] += 1
            mov_bl[1] -= 1
            ac += 1
        
        if (mov_tl[0]-1) >= 1 and (mov_tl[1]-1) >= 1 and [(mov_tl[0]-1), (mov_tl[1]-1)] not in o:
            mov_tl[0] -= 1
            mov_tl[1] -= 1
            ac += 1

        if (mov_br[0]+1) <= n and (mov_br[1]+1) <= n and [(mov_br[0]+1), (mov_br[1]+1)] not in o:
            mov_br[0] += 1
            mov_br[1] += 1
            ac += 1
    return ac

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    otacles = []

    for _ in range(k):
        otacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, otacles)

    fptr.write(str(result) + '\n')

    fptr.close()
