import sys, heapq

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()


def bin_search(n, A):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2
        if A[mid] == n:
            return 0, A[mid]
        elif A[mid] < n:
            start = mid + 1
        else:
            end = mid - 1

    diffs = []
    a = -1
    if start == mid + 1:
        if start < len(A):
            diffs.append((abs(n - A[start]), A[start]))
        diffs.append((abs(n - A[start - 1]), A[start - 1]))
    else:
        if end >= 0:
            diffs.append((abs(n - A[end]), A[end]))
        diffs.append((abs(n - A[end + 1]), A[end + 1]))
    diffs.sort()
    return diffs[0][0], diffs[0][1]


T = int(input())

for _ in range(T):
    k, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(4)]

    A = set()
    B = set()
    for i in board[0]:
        for j in board[1]:
            A.add(i + j)
    for i in board[2]:
        for j in board[3]:
            B.add(i + j)
    A = sorted(list(A))
    B = sorted(list(B))

    # print(A, B)
    mindiff = float('inf')
    x = -1

    for i in A:
        diff, a = bin_search(k - i, B)
        # print(diff, a + i)
        if diff < mindiff or diff == mindiff and x > a + i:
            mindiff = diff
            x = a + i


    # print(mindiff)
    print(x)
