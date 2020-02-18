#﻿17281 Baseball

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
else:
    import sys
    input = sys.stdin.readline
################################
def actionResult(inning, taza, ground, score, out):
    perform = results[inning][taza]
    if perform == 0:
        out += 1
    else:
        ground += 1
        for _ in range(perform):
            ground << 1
            if ground >= 16:
                score += 1
                ground -= 16
    return  ground,score,out

def play(startinning, roaster, ground, score, out):
    index = 0
    score = 0
    for inning in range(startinning,N):
        out = 0
        ground = 0
        while out < 3:
            taza = roaster[index]
            ground, score, out = actionResult(inning,taza,ground,score,out)
            #print('점수 추가 : ',score)
            index = (index + 1) % 9
    return score




def permuations(now, level, ground, score, out):
    if level == 9:
        global maxScore
        #print(now)
        score = play(now)
        #print(score)
        maxScore = max(maxScore,score)
        return

    for i in range(8):
        if chk[i]:
            continue
        next = now[:]
        if level == 3:
            next[level] = 0
            level += 1
        next[level] = nums[i]
        chk[i] = 1
        permuations(next, level + 1, ground, score, out)
        chk[i] = 0

N = int(input())
# 0 아웃, 1 안타, 2 2루타, 3 3루타, 4 홈런
results = [list(map(int,input().split())) for _ in range(N)]

nums = list(range(1,9))
chk = [0 for _ in range(8)]
maxScore = -1

permuations([0 for _ in range(9)],0,0,0,0)
print(maxScore)
