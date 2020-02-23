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
from itertools import product

def branchBound(height, level):
    global cnt

    for block in students[level]:
        nextHeight = height + block
        # print(nextHeight, level, cnt)
        if nextHeight >= H or level == N - 1:
            if nextHeight == H:
                # print('cnt')
                cnt += 1
                return
            if level == N - 1:
                continue
            return
        branchBound(nextHeight, level + 1)

N, M, H = map(int, input().split())
students = [[] for _ in range(N)]
for i in range(N):
    students[i] = sorted([0] + list(map(int, input().split())))

x = list(product(*students))
print(x)