import sys

input = lambda: sys.stdin.readline().rstrip()
f = open('output.txt', 'w')
# input = lambda: f.readline().rstrip()


def DFS(level, ptr):
    global maxnow, leftchk
    if leftchk % 2 == 0:
        return
    while ptr < M and now[ptr] == nums[ptr]:
        ptr += 1
    if level == K or ptr == M:
        if ptr == M:
            left = K - level
        else:
            left = -1
        if left >= 0:
            if leftchk < 0:
                leftchk = left % 2
            elif leftchk % 2 and left % 2 == 0:
                leftchk = 0
            return


        flag = False
        for i in range(M):
            if now[i] > maxnow[i]:
                flag = True
                break
            elif now[i] < maxnow[i]:
                break

        if flag:
            maxnow = now[:]
        return

    maxn = -1
    maxi = []
    for i in range(ptr, M):
        if now[i] >= maxn:
            if now[i] > maxn:
                maxi = []
            maxn = now[i]
            maxi.append(i)

    for i in maxi:
        now[i], now[ptr] = now[ptr], now[i]
        DFS(level + 1, ptr)
        now[i], now[ptr] = now[ptr], now[i]

# N, K = map(int, input().split())
string = '['
for K in range(1, 11):
    print(K)
    string += '['
    for N in range(1, 1000001):
        if N <= 10 or N < 100 and N % 10 == 0:
            # print(-1)
            string += '-1'
        else:
            dup = False
            now = []
            before = ''
            for c in str(N):
                if int(c) in now:
                    dup = True
                now.append(int(c))
                before = c
            nums = sorted(now, reverse=True)
            M = len(nums)

            leftchk = -1
            maxnow = now[:]
            DFS(0, 0)

            if leftchk >= 0:
                if leftchk % 2 and not dup:
                    nums[-1], nums[-2] = nums[-2], nums[-1]
                    maxnow = nums
                else:
                    maxnow = nums
            # print(leftchk)
            for n in maxnow:
                # print(n, end='')
                string += str(n)
        # print(end=' ')
        string += ','
    # print()
    # string += '\n'
    string += '],'
string += ']'
f.write(string)