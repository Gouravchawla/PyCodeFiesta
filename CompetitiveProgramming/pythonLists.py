# Url: https://www.hackerrank.com/challenges/python-lists

L = []
inpList = []

N = eval(input())

for i in range(N):
    inpList = input().split()

    if inpList[0] == 'insert':
        L.insert(eval(inpList[1]), eval(inpList[2]))
    elif inpList[0] == 'append':
        L.append(eval(inpList[1]))
    elif inpList[0] == 'remove':
        L.remove(eval(inpList[1]))
    elif inpList[0] == 'pop':
        L.pop()
    elif inpList[0] == 'index':
        L.index(eval(inpList[1]))
    elif inpList[0] == 'count':
        L.count(eval(inpList[1]))
    elif inpList[0] == 'sort':
        L.sort()
    elif inpList[0] == 'reverse':
        L.reverse()
    elif inpList[0] == 'print':
        print(L)
            
