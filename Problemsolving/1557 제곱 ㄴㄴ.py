import sys
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


m, M = map(int, input().split())
check = [0] * (M - m + 1)

for i in range(2, int(M ** 0.5) + 1):
    po = i * i
    for j in range(((m - 1) // po + 1) * po, M + 1, po):
        # print(j, end=' ')
        check[j - m] = 1
    # print()

print((M - m + 1) - sum(check))
