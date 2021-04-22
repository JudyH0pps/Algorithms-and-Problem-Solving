import sys
sys.stdin = open('input.txt')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

cells = []
for r in range(N):
    for c in range(N):
        cells.append([board[r][c], r, c])
cells.sort(reverse=True)

answer = -1

for B, r, c in cells:
    near = []
    if 0 <= r - 1 and board[r][c] < board[r - 1][c]:
        near.append(visit[r - 1][c])
    if 0 <= c - 1 and board[r][c] < board[r][c - 1]:
        near.append(visit[r][c - 1])
    if r + 1 < N and board[r][c] < board[r + 1][c]:
        near.append(visit[r + 1][c])
    if c + 1 < N and board[r][c] < board[r][c + 1]:
        near.append(visit[r][c + 1])
    if near:
        visit[r][c] = max(near)
    visit[r][c] += 1
    answer = max(answer, visit[r][c])

print(answer)
