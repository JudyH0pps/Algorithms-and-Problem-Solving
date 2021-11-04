import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

R, C, N = map(int, input().split())

board = [list(input()) for _ in range(R)]

if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
else:
    for _ in range(N // 2):
        nboard = [['.'] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if board[r][c] == '.':
                    if (r - 1 < 0 or board[r - 1][c] == '.') and (r + 1 >= R or board[r + 1][c] == '.'):
                        if (c - 1 < 0 or board[r][c - 1] == '.') and (c + 1 >= C or board[r][c + 1] == '.'):
                            nboard[r][c] = 'O'
        board = nboard
    for line in board:
        print(''.join(line))
