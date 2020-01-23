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
    
    Mi = -1
    Mc = -1
    leng = len(days)

    #print(days)
    for day, cost in enumerate(days[:-1]):
        #print(day,cost)
        if day > Mi:
            tmp = days[day:]
            Mc = max(tmp)
            Mi = leng - tmp[::-1].index(Mc) - 1
        if cost < Mc:
            #print(day+1,'날',cost,'에 사서',Mc,'가격에 판다')
            earn += Mc - cost
                      
    print('#%d %d'%(test_case,earn))
            
        
