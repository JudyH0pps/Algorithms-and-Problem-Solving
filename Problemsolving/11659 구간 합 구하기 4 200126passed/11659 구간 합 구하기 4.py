# 백준 11659 구간 합 구하기 4

#####입력 모드
# 0 : txt모드 , 1: 제출용
import sys

INPUTMODE = 1
if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
else:
    input = sys.stdin.readline 
################################   


N, M = map(int,input().split())

nums = list(map(int,input().split()))
cumul = [0]
for i in range(N):
    cumul.append(cumul[i] + nums[i])

for _ in range(M):
    i,j = map(int,input().split())
    print(cumul[j]-cumul[i-1])

            
 
