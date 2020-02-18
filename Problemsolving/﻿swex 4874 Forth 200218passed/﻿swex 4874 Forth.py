# ﻿swex 4874 Forth

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
    s = input().split()


    def cacul(s):
        stack = []
        for char in s:
            if char == '.':
                if len(stack) > 1:
                    return "error"
                return stack.pop()
            elif char.isnumeric():
                stack.append(char)
            else:
                if len(stack) < 2:
                    return "error"
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(int(a) + int(b))
                elif char == '-':
                    stack.append(int(a) - int(b))
                elif char == '*':
                    stack.append(int(a) * int(b))
                elif char == '/':
                    stack.append(int(a) // int(b))


    print('#%d' % test_case, cacul(s))
