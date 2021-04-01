def dfs(level, score, last):
    if level == N:
        scores.add(score)
        return

    for i in range(last, 4):
        dfs(level + 1, score + roman[i], i)


roman = [1, 5, 10, 50]
N = int(input())
scores = set()
dfs(0, 0, 0)
print(len(scores))
