# 백준 7568 덩치


#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################


N = int(input())
people = [tuple(map(int,input().split())) for i in range(N)]
count = [1 for _ in range(N)]

for i in range(N):
    one = people[i]
    for j in range(i+1,N):
        two = people[j]
        #print(one,two)

        if one[0] > two[0] and one[1] > two[1]:
            #print('one이 더 큼')
            count[j] += 1
        elif one[0] < two[0] and one[1] < two[1]:
            #print('two이 더 큼')
            count[i] += 1
            
print(' '.join(map(str,count)))         
        
