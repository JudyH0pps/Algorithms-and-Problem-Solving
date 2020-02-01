# swex 1954 달팽이숫자
INPUTMODE = 1

if INPUTMODE:
    f = open('input.txt','r')
    input = f.readline
##################################

def printB(board):
    for i in range(N):
        for j in range(N):
            print('%d'%board[i][j],end=' ')
        print()

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    if N == 1:
        print('#%d'%test_case)
        print(1)
        continue
    board = [[0 for _ in range(N)]for _ in range(N)]
    row = 0
    col = 0
    numcnt = 1
    # 동, 남, 서, 북
    direction = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    distance = N-1
    while True:
        step = 0
        while step < distance:
            board[row][col] = numcnt
            numcnt += 1
            step += 1
            if direction == 3 and step >= distance:
                break
            row += dr[direction]
            col += dc[direction]
        #printB(board)
        #print('가야할 거리',distance)
        if numcnt > N**2:
            break
            
        direction = (direction + 1) % 4
        if direction == 0:
            row += dr[direction]
            col += dc[direction]
            distance -= 2
            if distance < 2:
                distance = 1
    print('#%d'%test_case)
    printB(board)
            
            
                
