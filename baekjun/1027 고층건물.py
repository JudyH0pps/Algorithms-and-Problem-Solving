import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

buildings = tuple(map(int, input().split()))
vision = [0] * N

for i in range(N - 1):
    slope = buildings[i + 1] - buildings[i]
    vision[i] += 1
    vision[i+1] += 1
    for j in range(i + 2, N):
        if buildings[j] > slope * (j - i) + buildings[i]:
            vision[i] += 1
            vision[j] += 1
            slope = round((buildings[j] - buildings[i]) / (j - i), 100)

print(max(vision))