import sys
sys.stdin = open('input.txt')

INF = 1000000000

# 3칸짜리 4
# 2칸짜리 ((N - 2) * 4 + (N - 1) * 4)
# 1칸짜리 ((N - 2) * (N - 2) + (N - 2) * (N - 1) * 4)

N = int(input())
die = list(map(int, input().split()))

if N == 1:
    print(sum(die) - max(die))
else:
    one = min(die)
    two = INF
    three = INF

    for a, b in [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]:
        two = min(two, die[a] + die[b])
    for a, b, c in [[0, 1, 3], [0, 1, 2], [1, 5, 3], [1, 5, 2], [4, 5, 2], [4, 5, 3], [0, 4, 2], [0, 3, 4]]:
        three = min(three, die[a] + die[b] + die[c])

    print(
        one * ((N - 2) * ((N - 2) + (N - 1) * 4)) +
        two * ((N - 2) * 4 + (N - 1) * 4) +
        three * 4
    )
