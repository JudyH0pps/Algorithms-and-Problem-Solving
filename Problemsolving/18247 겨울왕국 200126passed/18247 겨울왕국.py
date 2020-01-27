# 백준 18247 겨울왕국

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################   


T = int(input())

l4col = ord('l') - ord('a')

for _ in range(T):
    N, M = map(int,input().split())
    if N <= l4col or M < 4:
        print(-1)
    else:
        print(4 + l4col* M) 
