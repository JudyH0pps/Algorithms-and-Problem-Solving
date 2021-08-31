import sys
sys.stdin = open('input.txt')


def recur(nodes1, nodes2):
    print(nodes1, nodes2)
    if nodes1[-1] != nodes2[-1]:
        return False
    if len(nodes1) == 1:
        return True
    l = (len(nodes1) - 1) // 2
    return recur(nodes1[:l + 1], nodes2[:l + 1]) and recur(nodes1[l + 1:-1], nodes2[l + 1:-1])


T = int(input())

for tc in range(1, T+1):
    nodes1 = list(input().split())[:-1]
    nodes2 = list(input().split())[:-1]
    print(recur(nodes1, nodes2))
