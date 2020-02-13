#﻿swex 4866 괄호검사

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
    string = input()
    def gogosing():
        stack = []
        for c in string:
            if c == '{' or c == '(':
                stack.append(c)
            elif c == '}' or c == ')':
                if not stack:
                    print(0)
                    return
                left = stack.pop()
                if not((left,c) == ('(',')') or (left,c) == ('{','}')):
                    print(0)
                    return
        if stack:
            print(0)
        else:
            print(1)
    print('#%d'%test_case,end=' ')
    gogosing()
