import sys
sys.stdin = open('input.txt')


def getGDC(a, b):
    while b:
        n = a % b
        a = b
        b = n
    return a


def upperBound(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left


N, K = map(int, input().split())
A = list(map(int, input().split()))
maxVal = max(A)

ptr = 0

divisors = dict()

for n in range(1, int(K ** 0.5) + 1):
    for i in range(ptr, N):
        if K % n:
            continue
        if A[i] % n == 0:
            divisors[n] = divisors.get(n, [])
            divisors[n].append(i)
        if K // n != n and A[i] % (K // n) == 0:
            divisors[K // n] = divisors.get(K // n, [])
            divisors[K // n].append(i)

cnt = 0

# print(divisors)
for p in range(N - 2):
    for q in range(p + 1, N - 1):
        a = A[p] * A[q]
        gdc = getGDC(a, K)
        x = K // gdc
        if x not in divisors:
            continue
        r = upperBound(divisors[x], q)
        # print(A[p], A[q], a, x, A[q])
        # print(r, max(len(divisors[x]) - r, 0))
        cnt += max(len(divisors[x]) - r, 0)

print(cnt)
