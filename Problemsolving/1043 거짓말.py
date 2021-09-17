import sys
def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
know = list(map(int, input().split()))[1:]
myparty = [[] for _ in range(N + 1)]
knowvisit = [0] * (N + 1)

for k in know:
    knowvisit[k] = 1

party = []
partyvisit = [0] * M
answer = M
for _ in range(M):
    party.append(list(map(int, input().split()))[1:])
    for p in party[_]:
        myparty[p].append(_)

for k in know:
    for p in myparty[k]:
        if partyvisit[p]:
            continue
        answer -= 1
        partyvisit[p] = 1
        for o in party[p]:
            if knowvisit[o]:
                continue
            knowvisit[o] = 1
            know.append(o)

print(answer)
