import sys
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


def inverse(a, m):
    for i in range(1, m):
        if a * i % m == 1:
            return i


T = int(input())

for tc in range(1, T + 1):
    m1, m2, m3, a1, a2, a3 = map(int, input().split())
