# ﻿16637 괄호 추가하기

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
from itertools import permutations


def calculate(a, op, b):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


def findP(x):
    xp = parent[x]
    if x == xp:
        return x
    else:
        np = findP(xp)
        parent[x] = np
        return np


def union(x, y):
    x = findP(x)
    y = findP(y)
    if x > y:
        parent[x] = y
    elif x < y:
        parent[y] = x


N = int(input())
expression = input()
L = len(expression)
if L == 1:
    print(int(expression))
else:
    oriValue = [0] * L

    for i in range(0, L, 2):
        oriValue[i] = int(expression[i])

    maxAnswer = -2 ** 31

    for permutation in permutations(range(1, L, 2)):
    # for permutation in [(1, 3, 5, 7, 11, 13, 15, 17, 9)]:
        value = oriValue[:]
        parent = list(range(0, L))
        before = permutation[0]
        value[before - 1] = calculate(int(expression[before - 1]), expression[before], int(expression[before + 1]))
        parent[before] = before - 1
        parent[before + 1] = before - 1

        for order in permutation[1:]:
            leftP = findP(order - 1)
            a = value[leftP]
            rightP = findP(order + 1)
            b = value[rightP]
            op = expression[order]
            value[leftP] = calculate(a, op, b)
            parent[order] = leftP
            parent[order + 1] = leftP

        if maxAnswer < value[0]:
            # print(permutation)
            maxAnswer = value[0]

    print(maxAnswer)
