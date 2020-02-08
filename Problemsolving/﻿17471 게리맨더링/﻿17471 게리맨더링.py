#﻿17471 게리맨더링

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
graph = {}

N = int(input())
popul = list(map(int,input().split()))
for i in range(1,N+1):
    tmp = [*map(int,input().split())]
    graph[i] = tmp[1:]

print(graph)


