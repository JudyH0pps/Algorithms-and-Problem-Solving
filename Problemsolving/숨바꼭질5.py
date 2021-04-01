from collections import deque
import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())


sister = []

pos = K
jump = 0
while pos <= 500000:
    jump += 1
    sister.append([pos, jump])
    pos += jump

oddVisit = [0] * 500001
evenVisit = [0] * 500001

answer = []

q = deque()
q.append([1, N])
oddVisit[N] = 1
while q:
    time, pos = q.popleft()

    for npos in (pos - 1, pos + 1, pos * 2):
        if 0 > npos or npos > 500000:
            continue
        ntime = time + 1
        if ntime % 2:
            if oddVisit[npos]:
                continue
            oddVisit[npos] = ntime
            q.append([ntime, npos])
        else:
            if evenVisit[npos]:
                continue
            evenVisit[npos] = ntime
            q.append([ntime, npos])

for pos, time in sister:
    if time % 2 and time >= oddVisit[pos]:
        print(time - 1)
        break
    elif time % 2 == 0 and time >= evenVisit[pos]:
        print(time - 1)
        break
else:
    print(-1)
