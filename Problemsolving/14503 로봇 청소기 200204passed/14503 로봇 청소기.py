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

dir = ['△','▷','▽','◁']

def printB(borad):
    for i in range(N):
        for j in range(M):
            if i == rrow and j == rcol:
                print(dir[direction],end=' ')
            else:
                print(board[i][j],end=' ')
        print()
    print()

N,M = map(int,input().split())

rrow,rcol,direction = map(int,input().split())
# 0북, 1동, 2남, 3서
drow = [-1,0,1,0]
dcol = [0,1,0,-1]
board = [list(map(int,input().split())) for _ in range(N)]
cleaned = 0

find = False
while True:
    #printB(board)
    #현재 위치가 청소가 안되었다면 청소 : 9
    if board[rrow][rcol] != 9:
        board[rrow][rcol] = 9
        cleaned += 1
        
    #왼쪽 방향으로 4번 회전
    find = False
    for _ in range(4):
        direction = (direction - 1) % 4
        leftrow = rrow + drow[direction]
        leftcol = rcol + dcol[direction]
        #왼쪽이 청소가 안되었다면
        if board[leftrow][leftcol] == 0:
            rrow = leftrow
            rcol = leftcol
            find = True
            break
    if find:
        continue
    #4번 돌아서 제자리로 왔다면 뒤쪽이 비었는지 확인하고 후진
    backrow = rrow + drow[direction-2]
    backcol = rcol + dcol[direction-2]
    # 후진할 수 없다면 종료
    if board[backrow][backcol] == 1:
        break
    else:
        rrow = backrow
        rcol = backcol

print(cleaned)







    
