list = [ 0 for _ in range(10**6) ]

N = 11


for i in range(2,N+1):
    if i % 2 == 0:
        list[i] = min(list[i-1] + 1,list[i//2]+1)
        #if i == N:
            #print(list[i-1] + 1,list[i//2]+1)
    elif i % 3 == 0:
        list[i] = min(list[i-1] + 1, list[i//3]+1)
    else:
        list[i] = list[i-1] + 1
    print(list[:N+1])

print(list[N])
#print(list[N-1])
