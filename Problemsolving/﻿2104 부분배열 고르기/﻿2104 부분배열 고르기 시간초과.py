# ﻿2104 부분배열 고르기

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()

################################
import sys

sys.setrecursionlimit(10 ** 6)


def sub(start, end):
    # print(start,end)
    global maxAnswer
    if end - start <= 0:
        return -1
    elif end - start == 1:
        return A[start] ** 2

    minI = -1
    minVal = 1000001
    for i in range(start, end):
        if A[i] < minVal:
            minI = i
            minVal = A[i]
    answer = minVal * (cumul[end] - cumul[start])
    # print(answer)
    left = sub(start, minI)
    right = sub(minI + 1, end)
    return max(left, right, answer)


N = int(input())
A = list(map(int, input().split()))
cumul = [0] * (len(A) + 1)
cumul[1] = A[0]
for i in range(2, len(A) + 1):
    cumul[i] = cumul[i - 1] + A[i - 1]
# print(cumul)
answer = sub(0, len(A))
print(answer)
