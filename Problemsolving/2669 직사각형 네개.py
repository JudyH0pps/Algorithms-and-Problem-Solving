import sys
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


board = set()
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(x1, x2):
        for c in range(y1, y2):
            board.add((r, c))

print(len(board))
