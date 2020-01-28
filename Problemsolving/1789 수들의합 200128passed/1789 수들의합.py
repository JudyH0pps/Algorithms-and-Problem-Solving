#백준 1789 수들의합

S = int(input())

cumul = [0]
i = 0
while cumul[i] <= S:
    cumul.append(cumul[i]+i+1)
    i += 1

print(i-1)
