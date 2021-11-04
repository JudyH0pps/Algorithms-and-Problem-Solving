import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

operation = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: lambda x, y: (abs(x) // y) if x >= 0 else -(abs(x) // y),
}


def DFS(num, level):
    if level == N - 1:
        global M, m
        if M < num:
            M = num
        if m > num:
            m = num

    for i in range(4):
        if op[i] <= 0:
            continue
        op[i] -= 1
        next_num = operation[i](num, nums[level + 1])
        DFS(next_num, level + 1)
        op[i] += 1


N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

M = float('-inf')
m = float('inf')

DFS(nums[0], 0)
print(M)
print(m)