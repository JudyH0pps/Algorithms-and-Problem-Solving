#백준 14499 주사위 굴리기
import sys

def printd():
    for i in range(4):
        for j in range(3):
            if die[i][j] != -1:
                print(die[i][j],end='')
            else:
                print(' ',end='')
        print()
        
def roll(m):
    if m == 1:
        tmp = die[1][2]
        die[1].pop()
        die[1].insert(0,die[3][1])
        die[3][1] = tmp
    if m == 2:
        tmp = die[1][0]
        die[1].pop(0)
        die[1].append(die[3][1])
        die[3][1] = tmp
    if m == 3:
        tmp = die[0][1]
        for i in range(3):
            die[i][1] = die[i+1][1]
        die[3][1] = tmp
    if m == 4:
        tmp = die[3][1]
        for i in range(3,0,-1):
            die[i][1] = die[i-1][1]
        die[0][1] = tmp
        
def move(m): #동1 서2 북3 남4
    global x,y
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    nx = x + dx[m-1]
    ny = y + dy[m-1]

    #print(nx,ny)
    if not (nx>=0 and nx<N and ny>=0 and ny<M):
        return
    
    #print(x,y,'->',nx,ny)
    roll(m)
    x = nx
    y = ny
    nowboard = board[nx][ny]
    if nowboard == 0:
        board[nx][ny] = die[3][1]
    else:
        die[3][1] = nowboard
        board[nx][ny] = 0

    print(die[1][1])
    
line = sys.stdin.readline()
N,M,x,y,K = map(int,line.split())

board = []
for _ in range(N):
    line = sys.stdin.readline()
    tmp = list(map(int,line.split()))
    board.append(tmp)
line = sys.stdin.readline()
movelist = list(map(int,line.split()))

die = [[-1,0,-1],
       [0,0,0],
       [-1,0,-1],
       [-1,0,-1]]
#바닥 3,1 꼭대기 1,1

for i in movelist:
    move(i)
