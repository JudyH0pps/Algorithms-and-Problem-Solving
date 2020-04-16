from collections import defaultdict


def count_subnode(index):
    def DFS(now):
        count = value[now]
        if left_child[now] <= N:
            count += DFS(left_child[now])
        if right_child[now] <= N:
            count += DFS(right_child[now])
        return count

    return DFS(index)


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    left_child = list(range(0, N * 2 + 1, 2))
    right_child = list(range(1, N * 2 + 2, 2))
    value = [0] * (N + 1)

    for _ in range(M):
        index, val = map(int, input().split())
        value[index] = val

    print('#%d' % tc, count_subnode(L))
