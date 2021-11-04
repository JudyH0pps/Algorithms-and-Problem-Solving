import sys
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


def inverse(a, m):
    for i in range(1, m):
        if a * i % m == 1:
            return i


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    b = []
    m = []
    product = 1
    for _ in range(N):
        bi, mi = map(int, input().split())
        product *= mi
        b.append(bi)
        m.append(mi)

    result = 0
    for i in range(N):
        partialProduct = product // m[i]
        result = (b[i] * partialProduct *
                  inverse(partialProduct, m[i]) + result) % product

    print(result)
