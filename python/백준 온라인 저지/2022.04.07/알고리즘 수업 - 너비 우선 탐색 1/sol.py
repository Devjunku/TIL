from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n+1):
    graph[i].sort()

visited = [0 for _ in range(n+1)]

q = deque([r])
visited[r] = 1

cnt = 1
while q:
    node = q.popleft()
    for nxt in graph[node]:
        if visited[nxt] == 0:
            cnt += 1
            visited[nxt] = cnt
            q.append(nxt)


for i in range(1, n+1):
    print(visited[i])