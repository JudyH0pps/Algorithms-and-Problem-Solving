from collections import deque
import math

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(enumerate(map(lambda x : int(math.log2(int(x)))+1, input().split())))
    oven = arr[:N]
    arr = deque(arr[N:])
    minval = min(oven, key=lambda x: x[1])[1]

    while not (not arr and len(oven) == 1):
        remove = []
        for idx, item in enumerate(oven):
            i, pizza = oven[idx]
            pizza -= minval
            if pizza <= 0 and arr:
                oven[idx] = arr.popleft()
            elif pizza:
                oven[idx] = (i, pizza)
            else:
                remove.append(idx)
        minval = min(oven, key=lambda x: x[1])[1]

    print("#%d" % tc, oven[0][0] + 1)

