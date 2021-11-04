import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

N, Q = map(int, input().split())

foods = [tuple(map(int, input().split())) for _ in range(N)]
foods.sort()
# print(foods)

for _ in range(Q):
    u, v, x, y = map(int, input().split())

    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        now = foods[mid][0]
        if u == now:
            left = mid
            break
        elif now < u:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if start == mid + 1:
            left = start
        elif end == mid - 1:
            left = end + 1

    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        now = foods[mid][0]
        if v == now:
            right = mid
            break
        elif now < v:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if start == mid + 1:
            right = start - 1
        elif end == mid - 1:
            right = end



    next_foods = foods[left:right + 1]
    next_foods.sort(key=lambda k: k[1])
    # print(next_foods)

    start = 0
    end = len(next_foods) - 1
    maxstart = -1
    while start <= end:
        mid = (start + end) // 2
        now = next_foods[mid][1]
        if x == now:
            left = mid
            break
        elif now < x:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if start == mid + 1:
            left = start
        elif end == mid - 1:
            left = end + 1

    start = 0
    end = len(next_foods) - 1

    while start <= end:
        mid = (start + end) // 2
        now = next_foods[mid][1]
        if y == now:
            right = mid
            break
        elif now < y:
            start = mid + 1
        else:
            end = mid - 1
    else:
        if start == mid + 1:
            right = start - 1
        elif end == mid - 1:
            right = end

    # print(next_foods[left:right + 1])
    # print('---')
    print(right - left + 1)
