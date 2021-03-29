N = int(input())
men = sorted(list(map(int, input().split())))
cumul = [0] * len(men)
cumul[0] = men[0]

for i in range(1, len(men)):
    men[i] += men[i-1]
    cumul[i] = men[i] + cumul[i-1]

print(cumul[-1])
