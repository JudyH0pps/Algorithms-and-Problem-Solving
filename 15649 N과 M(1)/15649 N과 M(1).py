# 15649 N과 M(1)

from collections import deque as que
from copy import deepcopy

f = open("input.txt","r")
input = f.readline


def dfs(n,m,d):

    print(n,m,d,arr,visit)
    global st
    if d == m:
        for a in arr:
            st += str(a) + " "
        st += '\n'
        return

    for i in range(1,n+1):
        if not visit[i]:
            visit[i] = True
            arr[d] = i
            dfs(n,m,d+1) 
            visit[i] = False

    return  


N, M = map(int,input().split())

st = ''
arr = [0 for _ in range(M)]
visit = [False for _ in range(N+1)]

dfs(N,M,0)
print(st)

             
        
