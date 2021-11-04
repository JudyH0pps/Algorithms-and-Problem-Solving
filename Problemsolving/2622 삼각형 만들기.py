import math
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

answer = 0

for a in range(1, N // 3 + 1):
    if N // 2 - 2 * a >= 0:
        answer += (N - 3 * a) // 2 - (N - 4 * a) // 2
    else:
        answer += (N - 3 * a) // 2 + 1

print(answer)
