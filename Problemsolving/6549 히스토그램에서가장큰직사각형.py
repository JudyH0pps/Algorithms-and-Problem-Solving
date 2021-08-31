import sys
sys.stdin = open('input.txt')


def divide(l, r):
    if l > r:
        return -1
    if l == r:
        return arr[l]
    mid = (l + r) // 2
    if mid & 1 == 0 and mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
        mid += 1
    maxArea = arr[mid]
    minH = arr[mid]
    s = mid
    e = mid

    while s - 1 >= l and e + 1 <= r:
        if arr[s - 1] >= arr[e + 1]:
            s -= 1
            minH = min(minH, arr[s])
        else:
            e += 1
            minH = min(minH, arr[e])
        maxArea = max(maxArea, (e - s + 1) * minH)

    while e + 1 <= r:
        e += 1
        minH = min(minH, arr[e])
        maxArea = max(maxArea, (e - s + 1) * minH)
    while s - 1 >= l:
        s -= 1
        minH = min(minH, arr[s])
        maxArea = max(maxArea, (e - s + 1) * minH)

    maxArea = max(maxArea, divide(l, (l + r) // 2))
    maxArea = max(maxArea, divide((l + r) // 2 + 1, r))
    return maxArea


data = list(map(int, input().split()))
while data[0]:
    arr = data[1:]
    answer = divide(0, len(arr) - 1)
    print(answer)
    data = list(map(int, input().split()))
