# 백 14503 로봇 청소기

#####입력 모드
# 0 : txt모드 , 1: 제출용
import sys

INPUTMODE = 0
if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
else:
    input = sys.stdin.readline 
################################


def printB(borad):
    for i in range(N):
        for j in range(M):
            print(board[i][j],end=' ')
        print()
    print()

N,M = map(int,input().split())

rrow,rcol,direction = map(int,input().split())

# 0북, 1동, 2남, 3서

board = [list(map(int,input().split())) for _ in range(N)]

printB(board)

cleaned = 0

while True:

    if board[rrow][rcol] != 9:
        board[rrow][rcol] = 9
        cleaned += 1
    
