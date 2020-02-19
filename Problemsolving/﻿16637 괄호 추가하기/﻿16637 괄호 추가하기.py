#﻿16637 괄호 추가하기

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
from collections import deque

def calculate(expression):
    # print(expression)
    leng = len(expression)
    if leng == 1:
        return expression
    elif leng == 3:
        a,op,b = expression
        a = int(a)
        b = int(b)
        if op == '+':
            return [a + b]
        elif op == '-':
            return [a - b]
        elif op == '*':
            return [a * b]
    else:
        left = calculate(expression[0:-2])
        op = [expression[-2]]
        right = calculate(expression[-1:])
        return calculate(left + op + right)


N = int(input())
expression = list(input())

maxAnswer = -1

for i in range(1<<N//2,1<<(N//2+1)):
    x = bin(i)[2:].zfill(N//2+1)
    if x.count('1') % 2 == 0 and x[-1] == '1':
        for i,e in enumerate(x):
            open = True
            if e == '1':
                if open:
                    open = False
                    before = int(i)
                else:
                    if int(i) - before != 1:
                        break
                    open = True
        else:
            print(x)







