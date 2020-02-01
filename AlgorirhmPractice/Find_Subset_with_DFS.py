import copy

def everySubset(oriSet, subSet = [], last = 0):
    print(subSet)
    if last == len(oriSet)+1:
        return
    
    for i in range(last,len(oriSet)):
        next_subSet = copy.deepcopy(subSet)
        next_subSet.append(oriSet[i])
        everySubset(oriSet, next_subSet, i+1) 
        
if __name__ == '__main__':
    oriSet = [1,2,3,4,5]
    everySubset(oriSet)
        

     
