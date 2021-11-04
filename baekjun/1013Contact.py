import sys, heapq

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

T = int(input())
for _ in range(T):
    wave = list(map(int, input()))

    start = False

    idx = 0
    while idx < len(wave):
        # print(idx, start)
        if not start:
            if wave[idx] == 0:
                if idx + 1 >= len(wave) or wave[idx + 1] == 0:
                    print('NO')
                    break
                idx += 2
            else:
                if idx + 3 >= len(wave) or wave[idx + 1] == 1 or wave[idx + 2] == 1:
                    print('NO')
                    break
                idx += 3
                start = True
        else:
            if wave[idx] == 0 and idx + 1 == len(wave):
                print('NO')
                break
            if wave[idx] == 1:
                if idx + 1 < len(wave) and wave[idx + 1] == 0:
                    start = False
                elif idx + 3 < len(wave) and wave[idx + 1] == 1 and wave[idx + 2] == 0 and wave[idx + 3] == 0:
                    start = False
            idx += 1
    else:
        print('YES')








