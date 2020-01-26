def chk(x,y,brown,red):
    #print(x,y)
    if (x-2)*(y-2) != red:
        return False
    if x*2 + (y-2)*2 == brown:
        return True
    return False

def solution(brown, red):
    xSave = 3
    y = 3
    
    while True:
        x = xSave
        while True:
            #print(x,y)
            if chk(x,y,brown,red):
                return [x,y]
            x += 1
            if x * y > brown + red:
                break            
        y +=1
        xSave += 1 
    #return [x,y]

print(solution(10,2))
