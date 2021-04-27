import sys
sys.stdin = open('input.txt')

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


N = int(input())
preferences = [list(map(int, input().split())) for _ in range(N ** 2)]
x = {}
classRoom = [[0] * N for _ in range(N)]
for preference in preferences:
    n = preference[0]
    preference = preference[1:]
    x[n] = preference
    nextPlace = (-1, -1)
    maxLike = -1
    maxZero = -1
    for r in range(N):
        for c in range(N):
            if classRoom[r][c]:
                continue
            like = 0
            zero = 0
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if classRoom[nr][nc] in preference:
                    like += 1
                elif classRoom[nr][nc] == 0:
                    zero += 1
            if like > maxLike or like == maxLike and zero > maxZero:
                nextPlace = (r, c)
                maxLike = like
                maxZero = zero
    r, c = nextPlace
    classRoom[r][c] = n

scoreTable = [0, 1, 10, 100, 1000]
score = 0

for r in range(N):
    for c in range(N):
        student = classRoom[r][c]
        like = 0
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if classRoom[nr][nc] in x[student]:
                like += 1
        score += scoreTable[like]


print(score)
