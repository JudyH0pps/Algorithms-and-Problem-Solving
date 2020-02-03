#swex 1284 수도 요금 경쟁
INPUTMODE = 1

if INPUTMODE:
    f = open('input.txt','r')
    input = f.readline
##################################

T = int(input())
for test_case in range(1,T+1):
    P,Q,R,S,W = map(int,input().split())

    A = P * W

    if  W <= R:
        B = Q 
    else:
        B = Q + S*(W-R)
 
    print('#%d %d'%(test_case,min(A,B)))
 
 
