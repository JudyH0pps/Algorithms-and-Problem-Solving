# 백준 11660 구간 합 구하기

#####입력 모드
# 0 : txt모드 , 1: 제출용

INPUTMODE = 0
if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################   

def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print()
    print()
    
N, M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
#printB(board)

for _ in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    summing = 0
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            summing += board[x-1][y-1]

    print(summing)
            
