import sys
from collections import deque
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().rstrip()


while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    players = [0] * 10001
    for _ in range(N):
        for player in list(map(int, input().split())):
            players[player] += 1

    players = sorted(list(map(lambda x: [-x[1], x[0]], enumerate(players))))
    secondP = players[1][0]

    for point, player in players[1:]:
        if point != secondP:
            break
        print(player, end=' ')
    print()
