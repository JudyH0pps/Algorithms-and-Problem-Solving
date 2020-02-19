# ﻿3954 Brainf__k 인터프리터

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
from collections import deque

def minus():
    global pointer
    memory[pointer] = (memory[pointer] - 1) % 256


def plus():
    global pointer
    memory[pointer] = (memory[pointer] + 1) % 256

def left():
    global pointer
    pointer = (pointer - 1)%memSize
def right():
    global pointer
    pointer = (pointer + 1)%memSize
def printP():
    pass
def saveChar():
    global pointer, Iptr
    if Iptr >= inputSize:
        char = 255
    else:
        char = ord(I[Iptr])
    memory[pointer] = char
    Iptr += 1
def open():
    global pointer, PC
    if memory[pointer] == 0:
        PC = pair[PC]

def close():
    global pointer,PC
    if memory[pointer] != 0:
        PC = pair[PC]


func = {
    '-':minus,
    '+':plus,
    '<':left,
    '>':right,
    '.':printP,
    ',':saveChar,
    '[':open,
    ']':close
}

T = int(input())
for test_case in range(1, T + 1):
    memSize, codeSize, inputSize = map(int, input().split())
    memory = [0] * memSize
    pointer = 0
    code = input()
    codeVisit = [0]*len(code)
    pair = {}
    stack = deque()
    for i,c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            a = stack.pop()
            pair[a] = i
            pair[i] = a
    PC = 0
    I = input()
    Iptr = 0
    cnt = 0
    while PC < codeSize:
        nowfunc = func[code[PC]]
        nowfunc()
        codeVisit[PC] = 1
        PC += 1
        cnt += 1
        if cnt >= 50000000:
            last = -1
            for i in range(len(code)-1,-1,-1):
                if codeVisit[i] == 1:
                    last = i
                    break
            print('Loops',pair[last+1],last + 1)
            break
        # print(nowfunc,pointer,PC,Iptr,lastOpen,lastClose)
    else:
        print('Terminates')

