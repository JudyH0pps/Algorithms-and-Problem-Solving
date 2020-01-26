#백준 14501 퇴사
import sys
import copy
import time

#입력부
N = int(sys.stdin.readline())
time = []
pay = []
for _ in range(N):
    t, p = map(int,sys.stdin.readline().split())
    time.append(t)
    pay.append(p) 
##
#print(time)
#print(pay)
day = [0 for _ in range(N)]

for i in range(N):
    #print(i,time[i],pay[i])
    if i>=1 and day[i-1] > day[i]:
        day[i] = day[i-1]
    
    t = time[i]
    next = t + i - 1
    if next >= N:
        continue

    tmp = day[i-1] + pay[i]

    if day[next] < tmp or day[next] == 0:
        day[next] = tmp   
    #print(day)

print(day[N-1])
