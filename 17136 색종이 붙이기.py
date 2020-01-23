# 백준 17136 색종이 붙이기
from collections import deque as que
from copy import deepcopy

#grim = ['□','①','②','③','④','⑤']
def printB(board):
    print()
    for i in range(10):
        for j in range(10):
            now = board[i][j]
            print(now,end=' ')
        print()
    print()
        
board = [list(map(int,input().split())) for _ in range(10)]
printB(board)

size = [5]*5
print(size)

for r in range(10):
    for c in range(10):
        pass
        
        
