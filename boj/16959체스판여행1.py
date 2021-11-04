import heapq
import sys
sys.stdin = open('input.txt')

INF = 100000000

Rmove = [[0, 1], [1, 0], [-1, 0], [0, -1]]
Bmove = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
Nmove = [[1, 2], [2, 1], [-1, -2], [-2, -1],
         [1, -2], [-1, 2], [2, -1], [-2, 1]]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

cells = dict()

for r in range(N):
    for c in range(N):
        cells[board[r][c]] = (r, c)

minTime = [1] * 3

for i in range(1, N * N):
    sr, sc = cells[i]
    er, ec = cells[i + 1]
    visit = [[[0] * N for _ in range(N)] for _ in range(3)]
    q = []
    heapq.heappush(q, [minTime[0], sr, sc, 0])
    heapq.heappush(q, [minTime[1], sr, sc, 1])
    heapq.heappush(q, [minTime[2], sr, sc, 2])
    visit[0][sr][sc] = 1
    visit[1][sr][sc] = 1
    visit[2][sr][sc] = 1
    nextMinTime = [0] * 3
    while q:
        level, r, c, piece = heapq.heappop(q)
        if r == er and c == ec:
            nextMinTime[piece] = level
        if all(nextMinTime):
            break
        if piece != 0 and not visit[0][r][c]:
            visit[0][r][c] = 1
            heapq.heappush(q, [level + 1, r, c, 0])
        if piece != 1 and not visit[1][r][c]:
            visit[1][r][c] = 1
            heapq.heappush(q, [level + 1, r, c, 1])
        if piece != 2 and not visit[2][r][c]:
            visit[2][r][c] = 1
            heapq.heappush(q, [level + 1, r, c, 2])

        if piece == 0 or piece == 1:
            move = Rmove
            if piece == 1:
                move = Bmove
            for i in range(1, N):
                for dr, dc in move:
                    nr = r + dr * i
                    nc = c + dc * i
                    if not (0 <= nr < N and 0 <= nc < N) or visit[piece][nr][nc]:
                        continue
                    visit[piece][nr][nc] = 1
                    heapq.heappush(q, [level + 1, nr, nc, piece])
        else:
            for dr, dc in Nmove:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < N and 0 <= nc < N) or visit[piece][nr][nc]:
                    continue
                visit[piece][nr][nc] = 1
                heapq.heappush(q, [level + 1, nr, nc, piece])
    minTime = nextMinTime

print(min(minTime) - 1)
