#11559 Puyo Puyo
from collections import deque

def printB(board):
    for i in board:
        for j in i:
            print(j,end='')
        print()
    print()
    
def dfs(board,chk,x,y,color,path):
    chk[x][y] = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx >= 0 and nx < 6 and ny >= 0 and ny < 12:
            if not chk[nx][ny] and board[nx][ny] == color:
                path.append((nx,ny))
                dfs(board,chk,nx,ny,color,path)
                
def drop(board):
    for row in board:
        now = 0
        for _ in range(len(row)):
            if row[now] == '*':   
                row.remove('*')
                row.append('.')
            else:
                now += 1
    

def step(board):
    printB(board)
    
    chk =[[0 for _ in range(12)] for _ in range(6)]
    bomb = False
    
    for i in range(6):
        for j in range(12):
            now = board[i][j]
            if now == '.': break
            if chk[i][j]: continue
            path = [(i,j)]
            dfs(board,chk,i,j,now,path)
            if len(path)>=4:
                bomb = True
                for x in path:
                    board[x[0]][x[1]] = '*'
    drop(board)
    
    return bomb
                        
f = open("puyo.txt","r")


board = []
tmp = f.readline()

for i in tmp[:-1]:
    q = deque()
    q.append(i)
    board.append(q)

while True:
    tmp = f.readline()
    if not tmp:
        break
    for i,x in enumerate(tmp[:-1]):
        board[i].appendleft(x)

cnt = 0 
while step(board):
    cnt += 1

print(cnt)



        
