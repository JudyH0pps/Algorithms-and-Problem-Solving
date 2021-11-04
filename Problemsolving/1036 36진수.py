import sys
def input(): return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')


def ctoi(c):
    if '0' <= c <= '9':
        return int(c)
    return ord(c) - ord('A') + 10


def itoc(i):
    if 0 <= i <= 9:
        return str(i)
    return chr(i - 10 + ord('A'))


def to36(num):
    answer = []
    while num:
        answer.append(itoc(num % 36))
        num //= 36
    return answer


def to10(s):
    answer = 0
    d = 1
    for x in s[::-1]:
        answer += ctoi(x) * d
        d *= 36
    return answer


N = int(input())
chars = dict()
score = 0

words = []
for _ in range(N):
    word = input()
    words.append(word)
    d = 1
    for i in range(len(word) - 1, - 1, -1):
        score += ctoi(word[i]) * d
        chars[word[i]] = chars.get(word[i], 0)
        chars[word[i]] += d * (35 - ctoi(word[i]))
        d *= 36

K = int(input())
i = 0
plus = sorted(list(chars.items()), key=lambda x: [-x[1], x[0]])
for a, ps in plus:
    if i >= K:
        break
    score += ps
    i += 1

if score == 0:
    print(0)
else:
    print(''.join(to36(score)[::-1]))
