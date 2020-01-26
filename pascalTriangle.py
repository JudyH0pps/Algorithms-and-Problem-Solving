def nextLine(line):
    tmp = [1]
    for i in range(len(line)-1):
        tmp.append(line[i] + line[i+1])
    tmp.append(1)    
    return tmp

H = 10
line = [1]
sum = 0
for i in range(H):
    print(line)
    for x in line:
        sum += x
    print(sum)
    line = nextLine(line)

print(sum)
    
