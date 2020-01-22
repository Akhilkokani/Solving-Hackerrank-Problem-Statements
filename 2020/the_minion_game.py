# Problem Statement Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(w):
    s = k = 0
    v = ['A', 'E', 'I', 'O', 'U']
    
    for x in range( len(w) ):
        if w[x] in v:
            k += (len(w)-x)
        else:
            s += (len(w)-x)

    if s == k: print("Draw")
    else:
        if s > k: print("Stuart", s)
        else: print("Kevin", k)

if __name__ == '__main__':
    s = input()
    minion_game(s)