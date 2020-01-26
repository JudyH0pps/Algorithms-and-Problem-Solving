#13460 구슬 탈출 2
from collections import deque
from copy import deepcopy

zechul = 0

def left(oriboard,N,M):
    board = deepcopy(oriboard)
    chk = 0
    # 왼쪽
    for i in range(N-2):
        now = 0
        sak = False
        for j in range(M-2):
            tmp = board[i][j]
            if tmp == '#':
                sak = False
                now = j+1
            if sak:
                if board[i][j] == 'B':
                    chk = -1
                if chk != -1:
                    if board[i][j] == 'R':
                        chk = 1                   
                board[i][j] = '.'
                continue
            if tmp == 'B' or tmp =='R':
                if now == j:
                    now += 1
                    continue
                
                board[i][now] = tmp
                board[i][j] = '.'
                now += 1
            if tmp == 'O':
                sak = True
    return board,chk
    
def right(oriboard,N,M):
    board = deepcopy(oriboard)
    chk = 0
    # 오른쪽
    for i in range(N-2):
        now = M-3
        sak = False
        for j in range(M-3,-1,-1):
            #print(i,j)
            tmp = board[i][j]
            #print(tmp)
            if tmp == '#':
                sak = False
                now = j-1
            if sak:
                if board[i][j] == 'B':
                    chk = -1
                if chk != -1:
                    if board[i][j] == 'R':
                        chk = 1 
                board[i][j] = '.'
                continue
            if tmp == 'B' or tmp =='R':           
                if j == now:
                    now -= 1
                    continue
                board[i][now] = tmp
                board[i][j] = '.'
                now -= 1
            if tmp == 'O':
                sak = True
    return board, chk

def up(oriboard,N,M):
    board = deepcopy(oriboard)
    chk = 0
    # 위
    for i in range(M-2):
        now = 0
        sak = False
        for j in range(N-2):
            tmp = board[j][i]
            if tmp == '#':
                sak = False
                now = j+1
            if sak:
                if board[j][i] == 'B':
                    chk = -1
                if chk != -1:
                    if board[j][i] == 'R':
                        chk = 1     
                board[j][i] = '.'
                continue
            if tmp == 'B' or tmp =='R':       
                if j == now:
                    now += 1
                    continue
                board[now][i] = tmp
                board[j][i] = '.'
                now += 1
            if tmp == 'O':
                sak = True
    return board, chk

def down(oriboard,N,M):
    board = deepcopy(oriboard)
    chk = 0
    # 아래
    for i in range(M-2):
        now = N-3
        sak = False
        for j in range(N-3,-1,-1):
            #print(i,j)
            tmp = board[j][i]
            #print(tmp)
            if tmp == '#':
                sak = False
                now = j-1
            if sak:
                if board[j][i] == 'B':
                    chk = -1
                if chk != -1:
                    if board[j][i] == 'R':
                        chk = 1  
                board[j][i] = '.'
                continue
            if tmp == 'B' or tmp =='R':
                if j == now:
                    now -= 1
                    continue
                board[now][i] = tmp
                board[j][i] = '.'
                now -= 1
            if tmp == 'O':
                sak = True
    return board, chk

def printB(board,N,M):
    for i in range(N-2):
        for j in range(M-2):
            print(board[i][j],end = '')
        print()

if not zechul:    
    f = open("ballExodus2.txt","r")

# 입력받는 부분
if not zechul:
    line = f.readline()
    N,M = map(int,line.split())
else:
    N,M = map(int,input().split())
board = [[0 for _ in range(M-2)] for _ in range(N-2)]
if not zechul:
    f.readline()
else:
    input()
for i in range(N-2):
    if not zechul:
        line = f.readline()
    else:
        line = input()
    for j in range(1,len(line)-2):## 개행문자때문에   
        board[i][j-1] = line[j]   

#BFS부분
iter = 0
q = deque()
q.append((board,0,iter))
find = False
while True:
    if not q:
        break
    nowbo,chk,iter = q.popleft()
    if not zechul:
        #printB(nowbo,N,M)
        print('iter',iter,'chk',chk,'')
    if chk == 1:
        find = True
        break
    if chk == -1 or iter == 10:
        continue
    nextbo,chk = up(nowbo,N,M)
    if nextbo != nowbo:
        q.append((nextbo,chk,iter+1))
    nextbo,chk = down(nowbo,N,M)
    if nextbo != nowbo:
        q.append((nextbo,chk,iter+1))
    nextbo,chk = left(nowbo,N,M)
    if nextbo != nowbo:
        q.append((nextbo,chk,iter+1))
    nextbo,chk = right(nowbo,N,M)
    if nextbo != nowbo:
        q.append((nextbo,chk,iter+1))

if find:
    print(iter)
else:
    print(-1)
  
