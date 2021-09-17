import sys
def input(): return sys.stdin.readline().rstrip()


N = input()

if N == '0':
    print('0')
else:
    answer = []
    for c in N:
        c = int(c)
        for o in (4, 2, 1):
            answer.append(c // o)
            c &= (o - 1)
    flag = False
    for o in answer:
        if not flag and o == 1:
            flag = True
        if flag:
            print(o, end='')
