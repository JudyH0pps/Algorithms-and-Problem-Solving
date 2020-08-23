from collections import deque

T = int(input())

for tc in range(1, T + 1):
    nums, left = input().split()
    left = int(left)
    N = len(nums)
    M = int(''.join(sorted(nums, reverse=True)))
    mv = -1

    odd_visit = set()
    even_visit = set()

    q = deque()
    q.append((int(''.join(nums)), left))

    while q:
        nums, left = q.popleft()
        if left % 2 == 0:
            if M == nums:
                ans = nums
                break
            v = nums
            if mv < v:
                mv = v
        if left == 0:
            continue

        for i in range(N):
            for j in range(i + 1, N):
                nnums = list(str(nums))
                nnums[i], nnums[j] = nnums[j], nnums[i]
                nnums = int(''.join(nnums))
                if not left % 2 and nnums not in even_visit:
                    even_visit.add(nnums)
                    q.append((nnums, left - 1))
                elif left % 2 and nnums not in odd_visit:
                    odd_visit.add(nnums)
                    q.append((nnums, left - 1))
    else:
        ans = mv

    print('#%d' % tc, ans)
