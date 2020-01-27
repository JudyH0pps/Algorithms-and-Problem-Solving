# 1차원 list에서 구간 합(Prefix Sum) 구하기

> 정수로 이루어진 길이 N인 List에서 list[i]부터 list[j]까지 더하기



#### 먼저 떠오르는 방법

```python
list = [x for x in range(1,N+1)]
sum = 0
for index in range(i,j+1):
    sum += list[index]
print(sum)
```

- time complexity : O(N)
- 구해야할 구간이 M개라면? O(NM)



#### 누적 합 list를 구하면

```python
cumulativeSum = [0 for _ in range(N+1)]
for x in range(1,N+1):
    cumulativeSum[x] = cumulativeSum[x-1] + list[x-1]
sum = cumulativeSum[j+1] - cumulativeSum[i]
```

- 누적 합 list 구하는 데 O(N)
- 구간 합 구하는 데 O(1)
- 구해야할 구간이 M개라면? O(N+M)
