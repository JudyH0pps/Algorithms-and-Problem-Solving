from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


delta = (
    (0, 1), (1, 0), (-1, 0), (0, -1)
)

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    stack = []

    for c in range(w):
        if board[0][c] == '.':
            stack.append([0, c])
        if board[h - 1][c] == '.':
            stack.append([h - 1, c])

    print(stack)
