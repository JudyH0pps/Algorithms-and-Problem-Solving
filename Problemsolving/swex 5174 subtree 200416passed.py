from collections import defaultdict


def count_subnode(index):
    def DFS(now):
        count = 1
        if children1[now]:
            count += DFS(children1[now])
        if children2[now]:
            count += DFS(children2[now])
        return count

    return DFS(index)


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    li = tuple(map(int, input().split()))
    children1 = defaultdict(int)
    children2 = defaultdict(int)

    for i in range(0, len(li), 2):
        parent = li[i]
        child = li[i + 1]
        if children1[parent]:
            children2[parent] = child
        else:
            children1[parent] = child

    print('#%d' % tc, count_subnode(N))
