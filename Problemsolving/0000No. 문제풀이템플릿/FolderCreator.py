import os
import sys

namefile = open('문제번호와 이름.txt','r',encoding='UTF8')
name = namefile.readline().rstrip()
namefile.close()

os.mkdir('../'+name+'/')

firstinput = '#' + name +'\n'
firstinput += """
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
"""

pythonfile = open('../'+name+'/'+name+'.py','w',encoding='UTF8')
pythonfile.write(firstinput)
pythonfile.close()

inputfile = open('../'+name+'/input.txt','w')
inputfile.close()