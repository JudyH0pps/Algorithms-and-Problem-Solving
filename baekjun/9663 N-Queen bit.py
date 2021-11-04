import sys

input = lambda: sys.stdin.readline().rstrip()


# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

def DFS(level, forward, leftdown, rightdown):
    if level == N:
        global cnt
        cnt += 1
        return

    add = forward | leftdown | rightdown

    for i in range(N):
        k = 1 << i
        if add & k == 0:
            DFS(level + 1, forward | k, (leftdown | k) << 1, (rightdown | k) >> 1)

N = int(input())

cnt = 0
DFS(0, 0, 0, 0)
print(cnt)
