import sys
def input(): return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')


def findP(x):
    if parent[x] == x:
        return x
    parent[x] = findP(parent[x])
    return parent[x]


N = int(input())

parent = [x for x in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, input().split())
    a = findP(a)
    b = findP(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(2, N + 1):
    if findP(parent[i]) != 1:
        print(1, parent[i])
        break
