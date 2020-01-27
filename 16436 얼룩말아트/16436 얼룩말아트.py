# 16436 얼룩말아트

############# 입력모드
# 0 : txt 모드 1: 제출

INPUTMODE = 0
if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline

##################################
    
def printB(board):
    for i in range(H):
        for j in range(W):
            print(board[i][j],end=' ')
        print()
    print()

W, H, K = map(int,input().split())
board = [[0 for _ in range(W)] for _ in range(H)]
printB(board)
        
for _ in range(K):
    ty,px,py,qx,qy = map(int,input().split())
    
    
