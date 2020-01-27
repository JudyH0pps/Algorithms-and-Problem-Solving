graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
            #인접 노드들을 큐에 넣는 과정
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start,[start])] #큐에는 (현재 노드, 밟아온 경로)를 저장
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            # 현재 노드가 최종 목표라면 종료하고 result에 추가
            result.append(path)
        else:
            for m in graph[n] - set(path):
                #현재 노드와 인접한 노드 중 밟아온 노드를 제외한 노드를 선택
                queue.append((m,path + [m]))
                #지금까지 밟아 온 경로에 선택된 노드를 추가
            print(queue)
    return result

#print(bfs(graph, 'A'))
print(bfs_paths(graph,'A','F'))
            
