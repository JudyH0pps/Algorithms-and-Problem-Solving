import sys
import heapq
sys.stdin = open('input.txt')

primenumbers = []
check = [0] * 100001
check[0] = 1
check[1] = 1

for i in range(2, 100001):
    if check[i]:
        continue
    primenumbers.append(i)
    for j in range(i + i, 100001, i):
        check[j] = 1


def isPrime(n):
    if n <= 100000 and check[n] == 0:
        return True
    if n & 1 == 0:
        return False
    for p in primenumbers:
        if n % p == 0:
            return False
    return True


def findP(x):
    if x == parent[x]:
        return x
    parent[x] = findP(parent[x])
    return parent[x]


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
hq = []
for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(hq, [c, a, b])

maxc = -1
while hq:
    c, a, b = heapq.heappop(hq)
    ap = findP(a)
    bp = findP(b)
    if ap == bp:
        continue
    maxc = max(maxc, c)
    if ap < bp:
        parent[bp] = ap
    else:
        parent[ap] = bp

while not isPrime(maxc):
    maxc += 1

print(maxc)
