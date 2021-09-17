import sys
def input(): return sys.stdin.readline().rstrip()


def getLine(sr, sc, nr, nc):
    global answer
    rd = nr - sr
    cd = nc - sc
    num = board[sr][sc]
    while 0 <= nr < N and 0 <= nc < M:
        num = num * 10 + board[nr][nc]
        if int(num ** 0.5) ** 2 == num and num > answer:
            answer = num
        nr += rd
        nc += cd


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
answer = -1

for sr in range(N):
    for sc in range(M):
        num = board[sr][sc]
        if int(num ** 0.5) ** 2 == num and num > answer:
            answer = num
        for nr in range(N):
            for nc in range(M):
                if sr == nr and sc == nc:
                    continue
                getLine(sr, sc, nr, nc)

print(answer)
