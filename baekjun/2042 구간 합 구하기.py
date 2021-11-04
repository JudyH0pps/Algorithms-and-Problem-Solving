import sys
f = open('input2042', 'r')
input = lambda: f.readline().rstrip()
# input = lambda: sys.stdin.readline().rstrip()

class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self):
        self.left = None
        self.right = None




N, M, K = map(int, input().split())

for _ in range(N):

