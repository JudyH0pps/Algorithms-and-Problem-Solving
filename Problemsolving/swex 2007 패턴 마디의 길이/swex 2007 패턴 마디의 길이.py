# swex 2007 패턴 마디의 길이
INPUTMODE = 1

if INPUTMODE:
    f = open('input.txt','r')
    input = f.readline
##################################

T = int(input())

for test_case in range(1,T+1):

    string = input().rstrip()
    tmp = ''

    for char in string:
        tmp += char

        x = string.split(tmp)

    
