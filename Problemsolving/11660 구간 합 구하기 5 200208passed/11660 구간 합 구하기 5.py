#11660 구간 합 구하기 5

import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

board = [[0 for _ in range(N+1)] for _ in range(N+1)]
for r in range(1,N+1):
    board[r] = [0] + list(map(int,input().split()))

for r in range(1,N+1):
        for i in range(1,N+1):
            board[r][i] += board[r][i-1] + board[r-1][i] - board[r-1][i-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    tmp = board[x2][y2] + board[x1-1][y1-1] - board[x1-1][y2] - board[x2][y1-1]
    print(tmp)