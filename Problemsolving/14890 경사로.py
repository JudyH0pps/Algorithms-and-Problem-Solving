import sys
sys.stdin = open('input.txt')


def isPossible(line):
    visit = [0] * N
    for i in range(1, N):
        if abs(line[i] - line[i - 1]) >= 2:
            return False
        elif line[i] - line[i - 1] == 1:
            for k in range(L):
                if not (0 <= i - 1 - k < N) or line[i - 1 - k] != line[i - 1] or visit[i - 1 - k]:
                    return False
                visit[i - 1 - k] = 1
        elif line[i - 1] - line[i] == 1:
            for k in range(L):
                if not (0 <= i + k < N) or line[i + k] != line[i] or visit[i + k]:
                    return False
                visit[i + k] = 1
    return True


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for line in board:
    if isPossible(line):
        cnt += 1

for r in range(N - 1):
    for c in range(r + 1, N):
        board[r][c], board[c][r] = board[c][r], board[r][c]

for line in board:
    if isPossible(line):
        cnt += 1

print(cnt)
