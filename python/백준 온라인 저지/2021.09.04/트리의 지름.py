import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

graph = {i:[] for i in range(n+1)}

for _ in range(n-1):
    s, e, c = map(int, input().split())
    graph[s-1].append((e-1, c))
    graph[e-1].append((s-1, c))

def bfs(start):
    q = deque([(start, 0)])
    visited = [0] * n
    visited[start-1] = 1
    value = [0, 0]
    while q:
        s, c = q.popleft()

        for node_info in graph[s]:
            nxt, cost = node_info[0], node_info[1]
            if not visited[nxt-1]:
                visited[nxt-1] = 1
                q.append((nxt, cost+c))
                if value[1] < cost+c:
                    value[1] = cost+c
                    value[0] = nxt
    return value
    
f = bfs(1)
res = bfs(f[0])

print(res[1])