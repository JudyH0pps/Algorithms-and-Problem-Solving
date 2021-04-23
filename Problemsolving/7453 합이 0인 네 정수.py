import sys
sys.stdin = open('input.txt')


N = int(input())

board = [[] for _ in range(4)]
A = []
cnt = {}

for _ in range(N):
    nums = list(map(int, input().split()))
    for i in range(4):
        board[i].append(nums[i])

for a in board[0]:
    for b in board[1]:
        A.append(a + b)

for c in board[2]:
    for d in board[3]:
        cnt[c + d] = cnt.get(c + d, 0) + 1

answer = 0
for x in A:
    answer += cnt.get(-x, 0)

print(answer)
