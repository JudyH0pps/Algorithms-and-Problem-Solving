from collections import defaultdict
import sys

sys.stdin = open('input.txt')


INF = 100000000

delta = [
    [1, 2], [1, -2], [-1, 2], [-1, -2],
    [2, 1], [2, -1], [-2, 1], [-2, -1]
]


def dfs(level, r, c, tr, tc, visit):
    if r == tr and c == tc:
        return level
    if level == 3:
        return INF

    minLevel = INF
    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and not visit[nr, nc]:
            visit[nr, nc] = 1
            l = dfs(level + 1, nr, nc, tr, tc, visit)
            minLevel = min(minLevel, l)
    return minLevel


def AtoB(start, end, piece):
    sr, sc = start
    er, ec = end
    if piece == 'K':
        return dfs(0, sr, sc, er, ec, defaultdict(int))
    elif piece == 'B':
        if sr + sc == er + ec or sr - sc == er - ec:
            return 1
    else:
        if sr == er or sc == ec:
            return 1
        return 2
    return INF


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

nums = {}

for r in range(N):
    for c in range(N):
        nums[board[r][c]] = [r, c]

# 0 - R, 1 - B, 2 - K
piece = ['R', 'B', 'K']
pieces = [1, 1, 1]
for n in range(1, N ** 2):
    start = nums[n]
    end = nums[n + 1]
    nextpieces = [0] * 3
    mintime = INF
    for i in range(3):
        time = AtoB(start, end, piece[i])
        present = pieces[i]
        if time != INF:
            mintime = min(mintime, present + time)
            nextpieces[i] = present + time

    for i in range(3):
        if nextpieces[i]:
            nextpieces[i] = min(nextpieces[i], mintime + 1)
        else:
            nextpieces[i] = mintime + 1

    pieces = nextpieces
    # print(n + 1, pieces)

print(min(pieces) - 1)
