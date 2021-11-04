import sys

input = lambda: sys.stdin.readline().rstrip()


# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

def DFS(level):
    if level == N:
        global cnt
        cnt += 1
        return
    for c in range(N):
        if cols[c] or board[level][c]:
            continue
        cols[c] = 1
        visits = []
        i = 1
        for vr in range(level + 1, N):
            if c - i >= 0 and not board[vr][c - i]:
                board[vr][c - i] = 1
                visits.append((vr, c - i))
            if c + i < N and not board[vr][c + i]:
                board[vr][c + i] = 1
                visits.append((vr, c + i))
            i += 1
        DFS(level + 1)
        cols[c] = 0
        for vr, vc in visits:
            board[vr][vc] = 0


N = int(input())

cols = [0] * N
board = [[0] * N for _ in range(N)]
cnt = 0
DFS(0)
print(cnt)
