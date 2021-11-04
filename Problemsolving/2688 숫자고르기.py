import sys
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


N = int(input())
arr = [0] * (N + 1)

for i in range(1, N + 1):
    arr[i] = int(input())

answer = []

for i in range(1, N + 1):
    visit = [0] * (N + 1)
    visit[i] = 1
    n = arr[i]
    while not visit[n]:
        visit[n] = 1
        n = arr[n]
    if n == i:
        answer.append(i)

print(len(answer))
for n in answer:
    print(n)
