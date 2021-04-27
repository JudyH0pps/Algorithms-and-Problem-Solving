import sys
sys.stdin = open('input.txt')

T = int(input())


for _ in range(T):
    sm, sc, si = map(int, input().split())
    code = input()
    inputText = input()

    warp = [-1] * sc
    stack = []
    for idx, c in enumerate(code):
        if c == '[':
            stack.append(idx)
        elif c == ']':
            openIdx = stack.pop()
            warp[openIdx] = idx
            warp[idx] = openIdx

    cnt = 0
    ptr = 0
    while ptr < sc or cnt >= 50000000:
        print(cnt)
        cnt += 1
        if code[ptr] in ['[', ']']:
            ptr = warp[ptr]
        else:
            ptr += 1

    print(ptr)
