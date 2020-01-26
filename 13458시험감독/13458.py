#백준 13458
import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
B, C = map(int,sys.stdin.readline().split())

cnt = 0

for i in nums:
    if i < B:
        continue
    now = i - B
    if now % C == 0:
        cnt += now // C
    else:
        cnt += now // C + 1

print(cnt + N)
