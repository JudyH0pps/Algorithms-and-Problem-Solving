# swex 1208 Flatten

for test_case in range(1,11):
    dump_limit = int(input())
    boxes = list(map(int,input().split()))
    height = [0 for _ in range(101)]
    low = min(boxes)
    high = max(boxes)
    for e in boxes:
        height[e] += 1
    for dump in range(1,dump_limit+1):
        if high - low <= 1:
            break
        height[low + 1] += 1
        height[low] -= 1
        if height[low] == 0:
            low += 1
        height[high - 1] += 1
        height[high] -= 1
        if height[high] == 0:
            high -= 1

    for i in range(101):
        if height[i]:
            low = i
            break
    for i in range(100,-1,-1):
        if height[i]:
            high = i
            break

    print('#%d'%test_case,high - low)
                    

   
