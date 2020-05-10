T = int(input())


def printB(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print()


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]
    printB(board)
