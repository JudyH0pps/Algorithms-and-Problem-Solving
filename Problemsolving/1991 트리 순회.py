import sys
sys.stdin = open('input.txt')


def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])


def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])


def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')


N = int(input())

graph = {}

for _ in range(N):
    parent, child1, child2 = input().split()
    graph[parent] = [child1, child2]

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
