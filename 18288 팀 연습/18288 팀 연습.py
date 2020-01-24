# 백준 18288 팀 연습

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################   

'''
A,B,C가 1번부터 N번까지의 문제를 나눠서 풀어야 한다

문제는 순서대로 풀어야함
A가 해결한 문제는 K의 배수
B는 문제를 연속해서 풀 수 없다
C는 한 문제 이상 해결해야함

문제를 풀 수 있는 모든 방법의 수는?
'''
from collections import deque

N, K = map(int,input().split())

if K == 0:
    Alist = [0]
else:
    Alist = [x for x in range(1,N+1) if not x % K]

count = 0
solved = [0 for _ in range(N)]
nowi = 0
for Anum in Alist:
    q = deque()
    q.append((solved,nowi,Anum))
    while(True):
        if Anum == 0:
            nowsolved, nowAnum = q.pop()
        solved[nowi] = 'A'
        
        
        
