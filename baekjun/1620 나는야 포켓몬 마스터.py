import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

N, M = map(int, input().split())

pokedex = dict()

i = 0
for _ in range(N):
    i += 1
    name = input()
    pokedex[str(i)] = name
    pokedex[name] = i

for _ in range(M):
    query = input()
    print(pokedex[query])

