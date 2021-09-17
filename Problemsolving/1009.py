import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    x = a % 10
    for _ in range(b - 1):
        x = (a * x) % 10

    if x == 0:
        print(10)
    else:
        print(x)
