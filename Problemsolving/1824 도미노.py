import sys
sys.stdin = open('input.txt')


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.near = [None] * 4
        self.wall = 4

    def addWall(self, dir, nearNode):
        self.wall -= 1
        self.near[dir] = nearNode


def disconnect(a, b):
    if a > b:
        a, b = b, a


N, M = map(int, input().split())
nodes = [Node(_) for _ in range(N * M + 1)]

for i in range(1, N * M + 1):
    if i % M:
        nodes[i].addWall(1, nodes[i + 1])
        nodes[i + 1].addWall(3, nodes[i])
    if i + M <= N * M:
        nodes[i].addWall(2, nodes[i + M])
        nodes[i + M].addWall(0, nodes[i])
