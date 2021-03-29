N = int(input())
animals = list(map(int, input().split()))

A = set()
B = set()


def solve():
    Asum = 0
    Bsum = 0
    for animal in animals:
        if animal >= N:
            return 0
        if animal not in A:
            A.add(animal)
            Asum += animal
        elif animal not in B:
            B.add(animal)
            Bsum += animal
        else:
            return 0

    if Asum != sum(range(len(A))):
        return 0
    if Bsum != sum(range(len(B))):
        return 0

    if len(A) == len(B):
        return 2 ** min(len(A), len(B))
    else:
        return 2 ** (min(len(A), len(B)) + 1)


print(solve())
