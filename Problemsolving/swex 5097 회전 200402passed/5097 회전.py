T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ### 1번 풀이 : 나머지를 이용해서 구한 방법 ##
    # N번 회전시키면 다시 처음 상태와 똑같아지므로 M을 N으로 나눈 나머지를 구하면 답이됨
    # arr = tuple(map(int, input().split()))
    # print('#%d' % tc, arr[M % N])

    ### 2번 풀이 : front와 rear 변수를 이용해서 리스트를 큐로 사용 ###
    # front는 queue의 데이터가 들어있는 시작부분, rear는 마지막 데이터의 뒷부분
    # queue에서 데이터를 빼내면 front를 1 증가시켜줌
    # queue에 데이터를 push하면 rear를 1 증가시켜줌
    queue = list(map(int, input().split())) + [0] * 2000
    front = 0
    rear = N

    for _ in range(M):
        queue[rear] = queue[front] # 회전 : 데이터를 빼는 것과 동시에 뒷부분에 추가해줌
        front += 1
        rear += 1

    print('#%d' % tc, queue[front])
