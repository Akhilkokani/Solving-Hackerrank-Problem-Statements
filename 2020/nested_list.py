# Problem Statement Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if len(students) == 0: sclw = score
        else:
            if score < sclw: sclw = score

        students.append( [name, score] )

    sclw = min([x[1] for x in students if x[1] != sclw])

    students.sort(key = lambda x: x[0])
    
    for std in students:
        if std[1] == sclw:
            print(std[0])

