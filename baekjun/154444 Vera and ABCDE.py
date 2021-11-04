import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

line = ['***', '*.*', '*..']
blocks = [[0, 1, 0, 1, 1], [0, 1, 0, 1, 0], [0, 2, 2, 2, 0], [0, 1, 1, 1, 0], [0, 2, 0, 2, 0]]
alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

N = int(input())
s = input()

board = [''] * 5
for c in s:
    a = alphabet[c]
    for i, t in enumerate(blocks[a]):
        board[i] += line[t]

for line in board:
    print(line)
