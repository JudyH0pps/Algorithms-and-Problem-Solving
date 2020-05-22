import sys

sys.stdin = open('5250.txt')


def printB(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print()


import heapq

delta = (
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[float('inf')] * N for _ in range(N)]
    visit[0][0] = 0


    def bfs():
        q = []
        heapq.heappush(q, (0, 0, 0))
        while q:
            l, r, c = heapq.heappop(q)
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] > l + max(0, board[nr][nc] - board[r][c]) + 1:
                    visit[nr][nc] = l + max(0, board[nr][nc] - board[r][c]) + 1
                    heapq.heappush(q, (l + max(0, board[nr][nc] - board[r][c]) + 1, nr, nc))
        # printB(visit)
        return visit[N - 1][N - 1]


    print('#%d' % tc, bfs())
