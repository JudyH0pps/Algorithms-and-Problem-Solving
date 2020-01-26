message = 'Hello world!'

code = list(message)
code = [ord(x) for x in code]
xor = 0
sum = 0
#print(code)

for i in code:
    xor ^= i
    sum += i
print([bin(x) for x in code])
print(bin(xor))
print(bin(sum))
print(bin(int('0x2100045d',16)))
