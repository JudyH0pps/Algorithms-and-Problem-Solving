#﻿swex 5122 수열 편집

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
class Node:
    def __init__(self, value=None):
        self.value = value
        self.after = None

class LinkedList:
    length = 0

    def __init__(self):
        LinkedList.length = 0
        self.last = Node()
        self.start = self.last
        self.start.after = self.last

    def connect(self, aftervalue):
        after = Node(aftervalue)
        self.last.after = after
        self.last = after
        LinkedList.length += 1

    def insert(self, index, value):
        new = Node(value)
        if index == 0:
            new.after = self.start.after
            self.start.after = new
        else:
            now = self.start.after
            for _ in range(index):
                before = now
                now = now.after
            new.after = now
            before.after = new
        LinkedList.length += 1

    def delete(self, index):
        LinkedList.length -= 1
        if index == 0:
            tmp = self.start.after.after
            self.start.after = tmp
        else:
            now = self.start.after
            for _ in range(index):
                before = now
                now = now.after
            before.after = now.after

    def print(self, index=-1):
        now = self.start.after
        if index == -1:
            for _ in range(self.length):
                print(now.value,end=' ')
                now = now.after
            print()
        else:
            if index >= self.length:
                print(-1)
                return
            for _ in range(index):
                now = now.after
            print(now.value)

    def change(self, index, value):
        now = self.start.after
        for _ in range(index):
            now = now.after
        now.value = value

T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int, input().split())
    l_list = LinkedList()
    for value in map(int, input().split()):
        l_list.connect(value)
    for _ in range(M):
        action = input().split()
        index = int(action[1])
        if action[0] == 'D':
            l_list.delete(index)
        else:
            value = int(action[2])
            if action[0] == 'I':
                l_list.insert(index, value)
            elif action[0] == 'C':
                l_list.change(index, value)

    print('#%d'%tc,end=' ')
    l_list.print(L)