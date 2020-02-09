#﻿17472 다리 만들기 2

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################
def printB(board):
    for i in range(N):
        for j in range(M):
            print('%2d'%board[i][j],end=' ')
        print()
    print()

inputs = lambda : input().split()

# 동, 남, 서, 북
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def isWall(row, col):
    if 0 <= row < N and 0 <= col < M:
        return False
    return True

def findSB(row, col, end):
    minCnt = 11
    for i in range(4):
        cnt = 0
        nc = col + dc[i]
        nr = row + dr[i]
        while True:
            if isWall(nr,nc):
                break
            now = board[nr][nc]
            if now == 0:
                cnt += 1
                nc += dc[i]
                nr += dr[i]
                continue
            elif now == end:
                if cnt == 1:
                    break
                minCnt = min(minCnt,cnt)
            break
    return minCnt

def findShortestBridge(start, end):
    shortest = 11
    for i in range(N):
        for j in range(M):
            if board[i][j] == start:
                shortest = min(shortest,findSB(i,j,end))
    if shortest <= 1 or shortest >= 11:
        return
    global shortestLength
    shortestLength[(start,end)] = shortest

def makeIsland(row, col, isleNum):
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if isWall(nr,nc) or board[nr][nc] == 0 or board[nr][nc] == isleNum:
            continue
        board[nr][nc] = isleNum
        makeIsland(nr,nc,isleNum)

def findP(i):
    e = parents[i]
    if parents[i] == i:
        return i
    else:
        tmp = findP(e)
        parents[i] = tmp
        return tmp

def isUnion():
    before = findP(2)
    for i in range(3,isleNum+1):
        now = findP(i)
        if before != now:
            return False
        before = now
    return True

def union(x,y):
    x = findP(x)
    y = findP(y)
    if x < y:
        parents[y] = x
    elif y < x:
        parents[x] = y
    return parents

def allsubsets(now, last):
    global parents
    parents = [i for i in range(isleNum + 1)]
    #print('b',parents)
    for i in now:
        a, b = connects[i][0]
        parents = union(a,b)
    #print('a', parents)
    if isUnion():
        cumul = 0
        for i in now:
            cumul += connects[i][1]
            # print(connects[i][0],end=' ')
        # print('length :',cumul)

        global minLength
        minLength = min(minLength, cumul)

    for i in range(last+1,len(connects)):
        if i not in now:
            now.append(i)
            allsubsets(now, i)
            now.pop()

# Main #

N, M = map(int,inputs())
board = [list(map(int,input().split())) for _ in range(N)]
isleNum = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            isleNum += 1
            board[i][j] = isleNum
            makeIsland(i,j,isleNum)

shortestLength = {}
for i in range(2,isleNum+1):
    for j in range(i+1,isleNum+1):
        findShortestBridge(i,j)

# printB(board)
# print(shortestLength)
connects = tuple(shortestLength.items())
minLength = 101
parents = [i for i in range(isleNum + 1)]
allsubsets([],-1)

if minLength == 101:
    print(-1)
else:
    print(minLength)
