#백준 14500 테트로미노
import sys
import copy
import time

def Tblock(x,y,now):
    sum = now
    cnt = 0
    min = 4000
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if ny >=0 and ny < M and nx >=0 and nx < N:
            cnt += 1
            tmp = board[nx][ny]
            sum += tmp
            if tmp < min:
                min = tmp
    if cnt <= 2:
        return
    if cnt == 4:
        sum -= min
    global max
    if max < sum:
        max = sum
        
        
def dfs(x,y,cnt,sum,before):
    if cnt == 4:
        global max, count
        count += 1
        if max < sum:   
            max = sum
        return

    for d in range(4):
        if before == (d + 2)%4:
            continue           
        nx = x + dx[d]
        ny = y + dy[d]
        if ny >=0 and ny < M and nx >=0 and nx < N:# and not chk[nx][ny]
            dfs(nx,ny,cnt+1,sum+board[nx][ny],d)
            
    
N,M = map(int,sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
    
start = time.time()

#chk = [[0 for _ in range(M)] for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
max = -1
count = 0
for i in range(N):
    for j in range(M):
        #chk[i][j] = 1
        cnt = 1
        sum = board[i][j]
        before = -1
        dfs(i,j,cnt,sum,before)
        Tblock(i,j,sum)
end = time.time()
print(max)
#print(end - start,'초')
