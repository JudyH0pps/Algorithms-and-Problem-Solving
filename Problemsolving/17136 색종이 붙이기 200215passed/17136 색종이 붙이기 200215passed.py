# 백준 17136 색종이 붙이기
INPUTMODE = 1
if INPUTMODE:
    f = open('input.txt')
    input = lambda: f.readline().rstrip()


def printB(board):
    for i in range(10):
        for j in range(10):
            now = board[i][j]
            print(now, end=' ')
        print()
    print()


def boardChk(board):
    for i in range(10):
        for j in range(10):
            if board[i][j]:
                return False
    return True


def switch(row, col, large):
    for r in range(row, row + large):
        for c in range(col, col + large):
            board[r][c] = (board[r][c] + 1) % 2


def sizeChk(row, col, size):
    for r in range(row, row + size):
        for c in range(col, col + size):
            if not (0 <= r < 10 and 0 <= c < 10) or board[r][c] == 0:
                return False
    return True


def backtracking(row, col, level):
    # print(row,col,level)
    # printB(board)
    if boardChk(board):
        global minLevel
        minLevel = min(minLevel,level)
        return
    for c in range(col, 10):
        if board[row][c]:
            for size in range(5, 0, -1):
                if sizes[size - 1] > 0 and sizeChk(row, c, size):
                    switch(row, c, size)
                    sizes[size - 1] -= 1
                    # print(size, sizes)
                    backtracking(row, c, level + 1)
                    switch(row, c, size)
                    sizes[size - 1] += 1
            return

    for r in range(row + 1, 10):
        for c in range(10):
            if board[r][c]:
                for size in range(5, 0, -1):
                    if sizes[size - 1] > 0 and sizeChk(r, c, size):
                        switch(r, c, size)
                        sizes[size - 1] -= 1
                        # print(size, sizes)
                        backtracking(r, c, level + 1)
                        switch(r, c, size)
                        sizes[size - 1] += 1
                return


board = [list(map(int, input().split())) for _ in range(10)]
sizes = [5] * 5

minLevel = 1000

backtracking(0, 0, 0)

if minLevel == 1000:
    print(-1)
else:
    print(minLevel)

