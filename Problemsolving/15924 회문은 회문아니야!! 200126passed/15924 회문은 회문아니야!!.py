# 15924 회문은 회문아니야!!

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################


def palindromeChk(s):
    before = s[0]
    diff = False
    for r in range(len(s)//2+1):
        if s[r] != s[-(r+1)]:
            return False, diff
        if before != s[r]:
            diff = True
    return True,diff
    

S = input()
leng = len(S)

chk, diff = palindromeChk(S)
if chk:
    if diff:
        print(leng-1)
    else:
        print(-1)
else:
    print(leng)
    

   
