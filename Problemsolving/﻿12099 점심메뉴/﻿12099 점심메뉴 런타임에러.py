#﻿12099 점심메뉴

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

def printB(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            print(board[r][c],end=' ')
        print()
    print()

N, Q = map(int, input().split())
karamax = -1
amamax = -1
dish = []
for _ in range(N):
    kara, ama = map(int, input().split())
    dish.append((kara, ama))
gugan = []
for _ in range(Q):
    u, v, x, y = map(int, input().split())
    gugan.append((u, v, x, y))
    if v > karamax:
        karamax = v
    if y > amamax:
        amamax = y

board = [[0] * (amamax + 1) for _ in range(karamax + 1)]

for kara, ama in dish:
    board[kara][ama] = 1

for r in range(1,karamax+1):
    for c in range(1,amamax+1):
        board[r][c] += board[r][c - 1] + board[r - 1][c] - board[r - 1][c - 1]

# printB(board)
for u, v, x, y in gugan:
    print(board[v][y] + board[u - 1][x - 1] - board[u - 1][y] - board[v][x - 1])
