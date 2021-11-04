import sys
from collections import deque
# sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


def getO(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return [r, c]


def getHash(board):
    hash = 0
    for r in range(3):
        for c in range(3):
            hash = (hash << 4) + board[r][c]
    return hash


def getPuzzle(hash):
    puzzle = [[0] * 3 for _ in range(3)]
    for r in range(2, -1, -1):
        for c in range(2, -1, -1):
            puzzle[r][c] = hash & 15
            hash = hash >> 4
    return puzzle


delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]

end = getHash([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
board = [list(map(int, input().split())) for _ in range(3)]
o = getO(board)
board = getHash(board)
visit = set()
q = deque()
q.append([0, board, o])
visit.add(board)
flag = False
while q:
    time, board, o = q.popleft()
    if end == board:
        flag = True
        print(time)
        break
    puzzle = getPuzzle(board)
    for dr, dc in delta:
        nr = o[0] + dr
        nc = o[1] + dc
        if not (0 <= nr < 3 and 0 <= nc < 3):
            continue
        puzzle[o[0]][o[1]], puzzle[nr][nc] = puzzle[nr][nc], puzzle[o[0]][o[1]]
        phash = getHash(puzzle)
        if phash not in visit:
            visit.add(phash)
            q.append([time + 1, phash, [nr, nc]])
        puzzle[o[0]][o[1]], puzzle[nr][nc] = puzzle[nr][nc], puzzle[o[0]][o[1]]
if not flag:
    print(-1)
