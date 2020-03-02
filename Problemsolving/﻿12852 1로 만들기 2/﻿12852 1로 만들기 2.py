# ﻿12852 1로 만들기 2

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

N = int(input())
before = [-1] * (N + 1)


def BFS(N):
    q = deque()
    q.append((1, 0))
    while q:
        now, level = q.popleft()

        for next in (now * 3, now * 2, now + 1):
            if next <= N and before[next] == -1:
                if next == N:
                    before[next] = now
                    return level + 1
                before[next] = now
                q.append((next, level + 1))
print(BFS(N))
n = N
while n != -1:
    p = n
    print(p,end=' ')
    n = before[p]