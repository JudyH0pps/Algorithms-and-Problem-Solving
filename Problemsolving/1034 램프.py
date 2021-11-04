import sys
def input(): return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')


N, M = map(int, input().split())
board = [input() for _ in range(N)]
K = int(input())

maxScore = 0

rvisit = [0] * N
for r in range(N):
    if rvisit[r]:
        continue
    cnt = 0
    visit = [0] * M
    for c in range(M):
        if board[r][c] == '0':
            visit[c] = 1
            cnt += 1
    if (K & 1) != (cnt & 1) or K < M and K < cnt:
        continue
    score = 0
    for y in range(N):
        for x in range(M):
            if int(board[y][x]) ^ visit[x] == 0:
                break
        else:
            rvisit[y] = 1
            score += 1
    maxScore = max(score, maxScore)

print(maxScore)
