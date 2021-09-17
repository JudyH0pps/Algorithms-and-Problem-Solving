

def getHash(word):
    hash = 0
    for c in word:
        hash = (hash << 5) + ord(c) - ord('a') + 1
    return hash


print(getHash('judy'), bin(getHash('judy')))

print(getHash('nick'), bin(getHash('nick')))
