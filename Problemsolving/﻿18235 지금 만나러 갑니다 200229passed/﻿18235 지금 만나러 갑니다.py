# ﻿18235 지금 만나러 갑니다

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()
################################
from collections import deque

N, A, B = map(int, input().split())
right = max(A, B)
left = min(A, B)
diff = right - left
if diff % 2 == 1:
    print(-1)
else:
    x = diff // 2


    def BFS(x, left, right):
        q = deque()
        q.append((left, right, 1, 0))
        while q:
            left, right, jump, level = q.popleft()
            if x & (1 << level):
                nleft = left + jump
                nright = right - jump
                if nleft == nright:
                    return level + 1
                q.append((nleft, nright, jump * 2, level + 1))
            else:
                for i in (-1, 1):
                    nleft = left + jump * i
                    nright = right + jump * i
                    if 1 <= nleft <= N and 1 <= nright <= N:
                        q.append((nleft, nright, jump * 2, level + 1))
        return -1


    print(BFS(x, left, right))
