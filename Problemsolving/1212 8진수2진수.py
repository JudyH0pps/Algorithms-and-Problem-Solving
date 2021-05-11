import sys
sys.stdin = open('input.txt')

N = input()

answer = ''
for c in N:
    c = int(c)
    for o in (4, 2, 1):
        answer += str(c // o)
        c %= o

print(int(answer))
