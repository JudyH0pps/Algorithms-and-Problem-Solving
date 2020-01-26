from collections import deque

f = open("sample_input.txt","r")
def delNode(n,graph):
    for i in graph.values():
        if n in i:
            i.remove(n)
    remove(n)
    return
def endChk(n, graph):
    if len(graph[n]) < 2:
        delNode(n,graph)
        return True
    return False

T = int(f.readline())
for test_case in range(1,T+1):
    graph = {}
    st = deque()
    N = int(f.readline())
    for i in range(1,N+1):
        graph[i] = []
    for _ in range(N):
        a,b = map(int,f.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    if test_case != T:
        continue    
    print(graph)

    for i in graph.keys():
        if endChk(i,graph):
            continue
        now = i
        st.append(i)
        break
    
    while True:
        print(graph,st)
        
        
           
    print(st)
    print()
 
