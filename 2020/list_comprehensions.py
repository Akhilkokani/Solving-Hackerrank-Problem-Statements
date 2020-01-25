# Problem Statement Link: https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    ar = []
    p = 0

    for a in range(0,x+1): 
        for b in range(0,y+1): 
            for c in range(0,z+1):
                 if a + b + c != n:
                     ar.append( [a,b,c] )
    print(ar)

