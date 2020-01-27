# 15924 회문은 회문아니야!!

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################


def palindromeChk(s):
    for r in range(len(s)//2):
        if s[r] != s[-(r+1)]:
            return False
    return True
    

S = input()
leng = len(S)

find = False
ans = -1
for l in range(leng,0,-1):
    for start in range(leng - l + 1):
        #print(start,start+l)
        nowS = S[start:start+leng]
        if not palindromeChk(nowS):
            find = True
            ans = l
            break
    if find:
        break
print(ans)
    
    

   
