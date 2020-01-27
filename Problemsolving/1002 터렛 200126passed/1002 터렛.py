# 백준 1002 터렛

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################   

import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    R = max(r1,r2)
    r = min(r1,r2)

    if math.isclose(0,dist) and r == R:
        print(-1)
    elif math.isclose(dist,r+R) or math.isclose(dist,R-r):
        print(1)
    elif dist > r + R or dist < R - r:
        print(0)
    else:
        print(2)
                    

   
