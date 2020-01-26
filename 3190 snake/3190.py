#백준 3190 뱀
import sys

def printb(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end='')
        print()
    print()
N = int(sys.stdin.readline())
applenum = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(applenum):
    row, col = map(int,sys.stdin.readline().split())
    board[row-1][col-1] = 8
movenum = int(sys.stdin.readline())
moves = []
before = 0
for _ in range(movenum):
    a, b = sys.stdin.readline().split()
    moves.append((int(a) - before,b)) 
    before = int(a)

#뱀은 0,0에서 오른쪽으로 시작 D 시계 L 반시계
#방향 동 1 남 2 서 3 북 4
#보드 빈칸 0 사과8 머리 9

drow = [0,0,1,0,-1]
dcol = [0,1,0,-1,0]
    
headrow = 0
headcol = 0
tailrow = 0
tailcol = 0
direction = 1
end = False
time = 0

moves.append((N,'.'))

for move in moves:
    nextdir = move[1]
    for _ in range(move[0]):

        board[headrow][headcol] = direction
        
        nextrow = headrow + drow[direction]
        nextcol = headcol + dcol[direction]
        time += 1

        
        if not (nextrow >= 0 and nextrow < N and nextcol >= 0 and nextcol < N):
            end = True
            break
        next = board[nextrow][nextcol]
        if next == 1 or next == 2 or next == 3 or next == 4:
            end = True
            break
        if board[nextrow][nextcol] != 8:
            tmp = board[tailrow][tailcol]
            board[tailrow][tailcol] = 0
            tailrow += drow[tmp]
            tailcol += dcol[tmp]

        headrow = nextrow
        headcol = nextcol
        board[headrow][headcol] = 9
        #printb(board)

    if nextdir == 'D':
        direction += 1
        if direction == 5:
            direction = 1
    else:
        direction -= 1
        if direction == 0:
            direction = 4
    if end:
        break
        
print(time)
