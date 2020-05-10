T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    ans = ''
    for _ in range(12):
        # print(N, ans)
        N *= 2
        if N >= 1:
            ans += '1'
            N -= 1
        else:
            ans += '0'
        if not N:
            break
    print('#%d' % tc, end=' ')
    if N:
        print('overflow')
    else:
        print(ans)
