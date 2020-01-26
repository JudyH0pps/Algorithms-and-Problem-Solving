#백준 14500 테트로미노
import sys
import copy
import time

def inPathChk(x,y,path):
    for i in range(len(path)//6):
        if x == int(path[3*i:3*i+3]) and y == int(path[3*i+3:3*i+6]):
            return True
    return False

def dfs(path,cnt,sum):
    
    #print('함수체크',path,cnt,sum)
    if cnt == 4:
        global max
        if max < sum:
            max = sum
        return
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(len(path)//6):
        for d in range(4):
            
            nx = int(path[3*i:3*i+3]) + dx[d]
            ny = int(path[3*i+3:3*i+6]) + dy[d]
            if ny >=0 and ny < M and nx >=0 and nx < N and not chk[nx][ny]:# 
                if inPathChk(nx,ny,path):
                    continue
                tmp = path
                tmp += str('%03d'%nx) + str('%03d'%ny)
                dfs(tmp,cnt+1,sum+board[nx][ny])
            
    
N,M = map(int,sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

chk = [[0 for _ in range(M)] for _ in range(N)]
start = time.time()

max = -1
for i in range(N):
    for j in range(M):
        chk[i][j] = 1
        path = str('%03d'%i)+str('%03d'%j)
        cnt = 1
        sum = board[i][j]
        dfs(path,cnt,sum)
end = time.time()
print(max)
print(end-start,'초')
