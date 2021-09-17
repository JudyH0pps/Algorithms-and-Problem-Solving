import sys
sys.stdin = open('input.txt')


def lowerbound(arr, item):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return right


N = int(input())
crane = list(map(int, input().split()))
crane.sort()
M = int(input())
box = list(map(int, input().split()))
box.sort()

if crane[-1] < box[-1]:
    print(-1)
else:
    cnt = 0
    while box:
        cnt += 1
        for c in crane[::-1]:
            x = lowerbound(box, c)
            if x == -1:
                continue
            box.pop(x)
    print(cnt)
