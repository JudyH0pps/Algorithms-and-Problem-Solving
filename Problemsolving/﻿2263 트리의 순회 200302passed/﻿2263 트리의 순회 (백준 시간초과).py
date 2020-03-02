# ﻿2263 트리의 순회

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


def recur(instart, poststart, length):
    if length < 1:
        return
    # print(inorder[instart:instart + length], postorder[poststart:poststart + length])
    # print(instart, poststart)

    print(postorder[poststart + length - 1], end=' ')
    for i in range(instart, instart + length):
        if inorder[i] == postorder[poststart + length - 1]:
            pivot = i
            break

    recur(instart, poststart, pivot - instart)
    recur(pivot + 1, poststart + pivot - instart, length - pivot + instart - 1)


n = int(input())
inorder = tuple(map(int, input().split()))
postorder = tuple(map(int, input().split()))
recur(0, 0, len(inorder))
