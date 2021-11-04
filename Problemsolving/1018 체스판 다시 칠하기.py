import sys
def input(): return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [input() for _ in range(N)]

A = 1000

for sr in range(N - 7):
    for sc in range(M - 7):
        answer = [0, 0]
        for r in range(sr, sr + 8):
            for c in range(sc, sc + 8):
                if (r + c) & 1:
                    if board[r][c] == 'W':
                        answer[0] += 1
                    else:
                        answer[1] += 1
                else:
                    if board[r][c] == 'B':
                        answer[0] += 1
                    else:
                        answer[1] += 1
        A = min(A, min(answer))

print(A)
