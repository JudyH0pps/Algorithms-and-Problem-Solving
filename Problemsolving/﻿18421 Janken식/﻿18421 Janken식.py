# ﻿18421 Janken식

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
operlands = {
    '+': 0,
    '-': 1,
    '*': 2
}
plusdict = {
    ('R', 'R'): ['R', 'R', 'R'],
    ('R', 'S'): ['R', 'S', 'P'],
    ('R', 'P'): ['P', 'R', 'S'],
    ('S', 'R'): ['R', 'S', 'P'],
    ('S', 'S'): ['S', 'S', 'S'],
    ('S', 'P'): ['S', 'P', 'R'],
    ('P', 'R'): ['P', 'R', 'S'],
    ('P', 'S'): ['S', 'P', 'R'],
    ('P', 'P'): ['P', 'P', 'P']
}

def divede(expression):
    if len(expression) == 3:
        x, op, y = expression
        return plusdict[(x,y)][operlands[op]]

N = int(input())
expression = input()
answer = input()