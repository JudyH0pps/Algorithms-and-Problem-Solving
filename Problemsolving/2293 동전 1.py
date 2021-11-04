import sys
from collections import deque
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
coin = []
for _ in range(n):
    c = int(input())
    coin.append(c)
coin.sort()

for c in coin:
    for i in range(k + 1):
        if i - c >= 0:
            dp[i] = dp[i - c] + dp[i]

print(dp[-1])
