T = int(input())
for tc in range(1, T + 1):
    N, s = input().split()
    N = int(N)
    ans = ''
    for digit in s:
        if ord(digit) >= ord('A'):
            digit = ord(digit) - ord('A') + 10
        else:
            digit = int(digit)
        tmp = ''
        while digit > 0:
            tmp = str(digit % 2) + tmp
            digit //= 2
        if len(tmp) <= 4:
            tmp = '0' * (4 - len(tmp)) + tmp
        ans += tmp
    print('#%d' % tc, ans)