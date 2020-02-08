#﻿1717 집합의 표현

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################

def findParent(e):
    if e == parent[e]:
        return e
    else:
        parent[e] = findParent(parent[e])
        return parent[e]

def union(x, y):
    x = findParent(x)
    y = findParent(y)
    if x != y:
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

def isUnion(x, y):
    x = findParent(x)
    y = findParent(y)
    if x == y:
        return True
    return False

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    move, a, b = map(int,input().split())
    if move == 0:
        union(a,b)
    else:
        if isUnion(a,b):
            print('YES')
        else:
            print('NO')
