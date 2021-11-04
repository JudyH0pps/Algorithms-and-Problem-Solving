import sys, heapq

input = lambda: sys.stdin.readline().rstrip()
# f = open('input1011.txt', 'r')
# input = lambda: f.readline().rstrip()

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x

    n = 1
    while n * (n + 1) < dist:
        n += 1
    n -= 1

    diff = dist - n * (n + 1)
    cnt = n * 2
    if 0 < diff <= (n + 1):
        cnt += 1
    elif diff != 0:
        cnt += 2

    print(cnt)


