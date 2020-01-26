
def cal(sum,nums,path,now):


    #print(path)
    
    if len(nums) == now:
        #print('ok',path)
        if sum == 0:
            print(path)
        return 

    tmp = nums[now]
    path = str(tmp) + path
    cal(sum+tmp,nums,'+'+path,now+1)
    cal(sum-tmp,nums,'-'+path,now+1)
    #print('case2',sum) 

def recur(str):
    if len(str) == 8:
        print(str)
        return
    else:
        recur(str+'+')
        recur(str+'-')
        
    
    
nums = [1,6,7,6,1,4,5]

sum = 0
path = ''
#cal(0,nums,path,0)
recur('')

