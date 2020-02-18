from itertools import permutations
import sys
sys.stdin = open('input.txt')

N = int(input())

results = [list(map(int,input().split())) for _ in range(N)]
every = permutations(range(1,9))
maxScore = -1

# print(results)

for tasun in every:
    inning = 0
    out = 0
    score = 0
    board = 0
    i = 0
    while True:
        if i == 3:
            taza = 0
        elif i >= 4:
            taza = tasun[i - 1]
        else:
            taza = tasun[i]

        action = results[inning][taza]

        if action == 0:
            out += 1
            if out >= 3:
                out = 0
                inning += 1
                board = 0
                if inning >= N:
                    break
        else:
            board += 1
            for _ in range(action):
                # print(action,bin(board))
                board <<= 1
                if board >= 8:
                    score += 1
                    board -= 8

        i = (i+1)%9
    # print(score)
    maxScore = max(maxScore,score)

print(maxScore)

