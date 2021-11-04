N = int(input())

board = [[' '] * N for _ in range(N)]

for c in range(N):
    board[0][c] = '*'
    board[N - 1][c] = '*'

for r in range(1, N - 1):
    board[r][0] = '*'
    board[r][N - 1] = '*'
    board[r][r] = '*'
    board[r][N - r - 1] = '*'

for _ in board:
    print(''.join(_))
