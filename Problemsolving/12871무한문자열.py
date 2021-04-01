import sys
sys.stdin = open('input.txt')

s = input()
t = input()


def GCD(a, b):
    while b:
        n = a % b
        a = b
        b = n
    return a


def LCM(a, b):
    return a * b // GCD(a, b)


for i in range(LCM(len(s), len(t))):
    if s[i % len(s)] != t[i % len(t)]:
        print(0)
        break
else:
    print(1)
