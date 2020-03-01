# ﻿swex 5658 보물상자 비밀번호

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

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    S = input().rstrip()

    words = set()
    for pivot in range(N // 4):
        for start in range(pivot, pivot + N, N // 4):
            tmp = ''
            for i in range(start, start + N // 4):
                tmp += S[i % N]
            words.add(int(tmp,16))

    words = sorted(words)
    print('#%d' % test_case, words[-K])
