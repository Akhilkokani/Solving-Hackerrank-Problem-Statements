# Problem Statement Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print( max(list(set(a) - set([max(a)]))) )
