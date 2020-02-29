#﻿1032 명령 프롬프트

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
N = int(input())

words = [input().rstrip() for _ in range(N)]

answer = ''

for c in range(len(words[0])):
    char = words[0][c]
    for r in range(1,N):
        if char != words[r][c]:
            answer += '?'
            break
    else:
        answer += char

print(answer)
