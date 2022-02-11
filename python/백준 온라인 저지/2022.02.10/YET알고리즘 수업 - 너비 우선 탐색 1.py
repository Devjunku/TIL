import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

def bfs(start):
    q = deque([])
    q.append((start, 1))
    visited[start] = 1
    while q:
        node, cost = q.popleft()
        for idx, nxt_node in enumerate(graph[node]):
            if not visited[nxt_node]:
                visited[nxt_node] = cost + (idx+1)
                q.append((nxt_node,cost + (idx+1)))
         
bfs(r)

for v in range(1, n+1):
    print(visited[v])
