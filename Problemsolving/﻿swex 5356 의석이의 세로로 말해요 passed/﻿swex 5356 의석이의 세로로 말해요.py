#﻿swex 5356 의석이의 세로로 말해요

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################

T = int(input())

for test_case in range(1,T+1):

    words = [input() for _ in range(5)]
    maxlen = max(map(len,words))
    for i, word in enumerate(words):
        words[i] = word.ljust(maxlen,' ')
    #print(words)
    words = list(zip(*words))
    #print(words)

    print('#%d'%test_case,end=' ')
    answer = ''
    for word in words:
        for c in word:
            if c != ' ':
                answer += c
    print(answer.strip(' '))


