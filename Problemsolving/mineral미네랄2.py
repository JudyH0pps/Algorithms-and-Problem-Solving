import sys
def input(): return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def printB(board):
    for l in board:
        print(''.join(l))


def shoot(r):
    if toRight:
        rng = range(C)
    else:
        rng = range(C - 1, - 1, -1)
    for c in rng:
        if board[r][c] == 'x':
            board[r][c] = '.'
            break


def botdfs(r, c):
    stack = [[r, c]]
    visit[r][c] = 1
    while stack:
        r, c = stack.pop()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < R and 0 <= nc < C) or visit[nr][nc] or board[nr][nc] == '.':
                continue
            visit[nr][nc] = 1
            stack.append([nr, nc])


def dfs(r, c):
    minc = maxc = c
    stack = [[r, c]]
    visit[r][c] = 1
    while stack:
        r, c = stack.pop()
        maxr[c] = max(maxr[c], r)
        blocks.append([r, c])

        minc = min(minc, c)
        maxc = max(maxc, c)
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < R and 0 <= nc < C) or visit[nr][nc] or board[nr][nc] == '.':
                continue
            visit[nr][nc] = 1
            stack.append([nr, nc])
    return [minc, maxc]


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
toRight = True
N = int(input())
for row in list(map(int, input().split())):
    shoot(R - row)
    toRight = not toRight
    visit = [[0] * C for _ in range(R)]
    for c in range(C):
        if board[R - 1][c] == 'c':
            visit[R - 1][c] = 1
            continue
        botdfs(R - 1, c)
    for r in range(R - 1, 0, -1):
        for c in range(C):
            if board[r][c] == '.' or visit[r][c]:
                visit[r][c] = 1
                continue
            blocks = []
            maxr = [-1] * C
            minc, maxc = dfs(r, c)
            bottom = max(maxr)
            if bottom == R - 1:
                continue
            # printB(board)
            for br, bc in blocks:
                board[br][bc] = '.'
            # print(minc, maxc, maxr)

            fallh = -1
            for h in range(1, R - bottom):
                flag = True
                one = False
                for br, bc in blocks:
                    br = maxr[bc]
                    if board[br + h][bc] == 'x':
                        flag = False
                        break
                for bc in range(minc, maxc + 1):
                    br = maxr[bc]
                    if br + h == R - 1 or board[br + h + 1][bc] == 'x':
                        one = True
                if flag and one:
                    fallh = h
                    break

            for br, bc in blocks:
                board[br + fallh][bc] = 'x'
                visit[br + fallh][bc] = 1
            # printB(board)
printB(board)
