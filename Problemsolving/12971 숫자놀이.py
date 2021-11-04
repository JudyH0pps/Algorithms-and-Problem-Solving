import sys
from collections import deque
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        n = a % b
        a = b
        b = n
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


p1, p2, p3, x1, x2, x3 = map(int, input().split())

G = lcm(p1, p2)
G = lcm(G, p3)

answer = -1
for n in range(1, G + 1):
    if n % p1 == x1 and n % p2 == x2 and n % p3 == x3:
        answer = n
        break

print(answer)
