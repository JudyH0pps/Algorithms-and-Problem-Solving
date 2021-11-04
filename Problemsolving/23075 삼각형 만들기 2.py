import math
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

beforeanswer = 0
for N in range(120):
    answer = 0
    tmp = []
    for a in range(1, N // 3 + 1):
        if N // 2 - 2 * a >= 0:
            answer += (N - 3 * a) // 2 - (N - 4 * a) // 2
            if (N - 3 * a) // 2 - (N - 4 * a) // 2:
                tmp.append((N - 3 * a) // 2 - (N - 4 * a) // 2)
        else:
            answer += (N - 3 * a) // 2 + 1
            if (N - 3 * a) // 2 + 1:
                tmp.append((N - 3 * a) // 2 + 1)
    print(-beforeanswer + answer, end=', ')
    beforeanswer = answer
