# Problem Statement Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

from collections import OrderedDict as od

def merge_the_tools(string, k):
    t = len(string)//k
    for s_ in range(t):
        print( "".join(od.fromkeys(string[:k])) )
        string = string[k:]
        


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)