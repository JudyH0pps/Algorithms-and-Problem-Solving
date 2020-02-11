# 백준 18246 색종이와 쿼

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################

def printB(board):
    for x in range(xmax):
        for y in range(ymax):
            print(board[x][y],end= ' ')
        print()
    print()

N, M = map(int,input().split())
#print(N,M)

ymax = -1
xmax = -1

kami = []
for _ in range(N):
    y1,x1,y2,x2 = map(int,input().split())
    if x2 > xmax:
        xmax = x2
    if y2 > ymax:
        ymax = y2
    kami.append((y1,x1,y2,x2))
    
board = [[0 for _ in range(ymax)] for _ in range(xmax)]

for y1,x1,y2,x2 in kami:
    for x in range(x1,x2):
        for y in range(y1,y2):
            board[x][y] += 1
 
printB(board)

for _ in range(M):
    y1,x1,y2,x2 = map(int,input().split())
    maxkami = -1
    for x in range(x1,x2):
        for y in range(y1,y2):
            maxkami = max(maxkami,board[x][y])
    print(maxkami)

                    

   
