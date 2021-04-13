import sys
sys.stdin = open('input.txt')


def recur(preorder, inorder):
    if not preorder:
        return
    node = preorder[0]

    leftPreorder = []
    rightPreorder = []
    leftInorder = []
    rightInorder = []

    flag = False
    j = 1
    for i in range(len(preorder)):
        if inorder[i] == node:
            flag = True
        elif not flag:
            leftInorder.append(inorder[i])
            leftPreorder.append(preorder[j])
            j += 1
        else:
            rightInorder.append(inorder[i])
            rightPreorder.append(preorder[j])
            j += 1

    recur(leftPreorder, leftInorder)
    recur(rightPreorder, rightInorder)
    print(node, end=' ')


T = int(input())

for _ in range(T):
    N = int(input())
    graph = {}
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    recur(preorder, inorder)
    print()
