from collections import deque

answer = float('inf')


def solution(n, weak, dist):
    def cover(dist):
        cweak = weak[:]
        for i in range(1, len(weak)):
            cweak[i] += weak[0]
        idx = 0
        cnt = 0
        for m in dist:
            cnt += 1
            start = idx
            for i in range(start, len(weak)):
                if weak[i] > weak[start] + m:
                    idx = i
                    print(idx)
                    break
                if i == len(weak) - 1:
                    idx = len(weak) - 1
            if idx == len(weak) - 1:
                return cnt
        return -1

    def dfs(level, weak):
        if level == len(dist):
            global answer
            for _ in range(len(weak)):
                weak.rotate()
                cnt = cover(dist)
                answer = min(cnt, answer)
            return

        for i in range(level, len(dist)):
            dist[level], dist[i] = dist[i], dist[level]
            dfs(level + 1, weak)
            dist[level], dist[i] = dist[i], dist[level]

    weak = deque(weak)
    dfs(0, weak)

    return answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
