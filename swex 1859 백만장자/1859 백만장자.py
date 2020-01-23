# swex 1859 백만장자

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################



from collections import defaultdict

T = int(input())

for test_case in range(1,T+1):
    #print('test_case',test_case)
    
    N = int(input())
    days = list(map(int,input().split()))
    earn = 0
    
    M = max([(i,x) for i,x in enumerate(days)],key = lambda x : x[1])
    Mi,Mc = map(int,M)
    #print(M)
    
    for day, cost in enumerate(days[:-1]):
        #print(day,cost)
        if day > Mi:
            M = max([(i,x) for i,x in enumerate(days[day:])],key = lambda x : x[1])
            Mi, Mc = map(int,M)
        if cost < Mc:
            earn += Mc - cost
        #print(earn)
                      
    print('#%d %d'%(test_case,earn))
            
        
