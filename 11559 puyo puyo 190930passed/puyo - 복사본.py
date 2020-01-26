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
    for i in range(6):
        now = 0
        for _ in range(12):
            row = board[i][now]
            if row == '*':   
                board[i].remove('*')
                board[i].append('.')
            else:
                now += 1
    

def step(board):
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
                        
board = []
tmp = input()
for i in range(6):
    q = deque()
    q.append(tmp[i])
    board.append(q)

for _ in range(11):
    tmp = input()
    for i in range(6):
        board[i].appendleft(tmp[i])

cnt = 0 
while step(board):
    cnt += 1

print(cnt)



        
