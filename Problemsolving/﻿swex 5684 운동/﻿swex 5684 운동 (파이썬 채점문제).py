# ﻿swex 5684 운동

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

def DFS(startnode, node):
    global minL

    stack = deque()
    stack.append((node,0,0))
    start = 0
    cumul = 0
    while True:
        # print(stack)
        # print(visit)
        # print(node,start)
        for nextnode in range(start, N):
            W = graph[node][nextnode]
            if W and cumul + W < minL:
                # print(node,'->',nextnode)
                if visit[nextnode]:
                    if startnode == nextnode:
                        minL = cumul + W
                    continue
                visit[nextnode] ^= 1
                node = nextnode
                start = 0
                cumul += W
                stack.append((nextnode,nextnode+1,cumul))
                break
        else:
            visit[stack[-1][0]] ^= 1
            start = stack[-1][1]
            stack.pop()
            if not stack:
                break
            node = stack[-1][0]
            cumul = stack[-1][2]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split(' '))
    graph = [[0] * N for _ in range(N)]

    for _ in range(M):
        s, e, c = map(int, input().split(' '))
        graph[s - 1][e - 1] = c

    # print(graph)

    visit = [0] * N
    minL = 10000 * M
    for node in range(N):
        visit[node] ^= 1
        DFS(node, node)


    print('#%d' % test_case, minL)
