# ﻿17140 이차원 배열과 연산

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()


################################


def printB(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print()


def move(line):
    cnt = {}
    for e in line:
        if e == 0:
            continue
        if e in cnt:
            cnt[e] += 1
        else:
            cnt[e] = 1
    sol = []
    for a, b in sorted(cnt.items(), key=lambda x: (x[1], x[0])):
        sol += [a, b]
    return sol


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
t = 0
while t <= 100:
    if 0 <= r - 1 < len(A) and 0 <= c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        break
    if len(A) >= len(A[0]):
        newA = []
        maxl = -1
        for line in A:
            temp = move(line)
            newA.append(temp)
            maxl = max(maxl, len(temp))
        for i in range(len(newA)):
            newA[i] = newA[i] + [0] * (maxl - len(newA[i]))
    else:
        A = list(zip(*A))
        newA = []
        maxl = -1
        for line in A:
            temp = move(line)
            newA.append(temp)
            maxl = max(maxl, len(temp))
        for i in range(len(newA)):
            newA[i] = newA[i] + [0] * (maxl - len(newA[i]))
        newA = list(zip(*newA))
    A = newA
    # printB(A)
    t += 1


if t == 101:
    print(-1)
else:
    print(t)
