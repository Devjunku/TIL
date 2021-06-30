from collections import deque

V = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(V):
    info = list(map(int, input().split()))
    for i in range(1, len(info) - 2, 2):
        graph[info[0]].append((info[i], info[i+1]))


def bfs(start):
    visited = [-1] * (V+1)
    q = deque([start])
    visited[start] = 0
    _max = [0, 0]

    while q:
        s = q.popleft()

        for node, dist in graph[s]:
            if visited[node] == -1:
                visited[node] = visited[s] + dist
                q.append(node)
                if _max[0] < visited[node]:
                    _max = visited[node], node

    return _max

dist, node = bfs(1)
dist, node = bfs(node)
print(dist)


