from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

parent = { i:[] for i in range(1, N+1)}

visited = [0] * (N+1)



def bfs(s, pa):
    q = deque([(s, pa)])

    while q:
        s, pa = q.popleft()
        visited[s] = 1
        parent[s] = pa
        for start in graph[s]:
            if visited[start]:
                continue
            else:
                q.append((start, s))


bfs(1, 1)
for i in range(2, N+1):
    print(parent[i])



def dfs(s, pa):

    visited[s] = pa
    parent[s] = pa

    for start in graph[s]:
        if visited[start]:
            continue
        else:
            dfs(start, s)