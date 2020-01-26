#백준 14500 테트로미노
import sys
import copy
import time

def dfs(path,cnt,sum,before):
    

    if cnt == 4:
        #print('함수체크',path,cnt,sum)
        global max
        if max < sum:
            
            max = sum
        return
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for p in path:
        for d in range(4):
            if before == (d + 2)%4:
                continue
            
            nx = p[0] + dx[d]
            ny = p[1] + dy[d]
    
            if ny >=0 and ny < M and nx >=0 and nx < N and (nx,ny) not in path and not chk[nx][ny]:
                tmp = copy.deepcopy(path)
                tmp.append((nx,ny))
                dfs(tmp,cnt+1,sum+board[nx][ny],d)
            
    
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
        path = [(i,j)]
        cnt = 1
        sum = board[i][j]
        before = -1
        dfs(path,cnt,sum,before)
end = time.time()
print(max,end-start,'초')
