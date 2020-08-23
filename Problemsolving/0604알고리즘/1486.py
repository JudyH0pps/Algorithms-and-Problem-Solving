T = int(input())


def backtracking(level, height):
    if level == N:
        global min_diff
        if height >= B and min_diff > height - B:
            min_diff = height - B
        return

    backtracking(level + 1, height + H[level])
    backtracking(level + 1, height)


for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = sorted(list(map(int, input().split())), reverse=True)

    min_diff = float('inf')

    backtracking(0, 0)

    print('#%d'%tc, min_diff)
