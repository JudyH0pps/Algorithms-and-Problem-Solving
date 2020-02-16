#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################
def branchBound(left, level):
    global cnt
    # print(left,level,cnt)
    for block in students[level]:
        nextLeft = left - block
        if nextLeft <= 0 or level == N - 1:
            if nextLeft == 0:
                # print('cnt')
                cnt += 1
            continue
        branchBound(nextLeft, level + 1)

N, M, H = map(int, input().split())
students = [[] for _ in range(N)]
for i in range(N):
    students[i] = sorted([0] + list(map(int, input().split())),reverse = True)
cnt = 0
branchBound(H, 0)
print(cnt%10007)