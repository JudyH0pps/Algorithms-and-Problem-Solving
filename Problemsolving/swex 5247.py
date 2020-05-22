#5247 연산

from collections import defaultdict, deque

million = 1000000

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())


    def bfs(N, M):
        q = deque()
        visit = set()
        q.append((N, 0))
        visit.add(N)
        while q:
            now, level = q.popleft()

            if now == M:
                return level

            if not now + 1 in visit and now + 1 <= million:
                visit.add(now + 1)
                q.append((now + 1, level + 1))
            if not now - 1 in visit and now - 1 <= million:
                visit.add(now - 1)
                q.append((now - 1, level + 1))
            if not now * 2 in visit and now * 2 <= million:
                visit.add(now * 2)
                q.append((now * 2, level + 1))
            if not now - 10 in visit and now - 10 >= 1:
                visit.add(now - 10)
                q.append((now - 10, level + 1))


    print('#%d' % tc, bfs(N, M))
