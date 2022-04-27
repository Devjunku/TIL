import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m ,k, x = map(int, input().split())

INF = sys.maxsize

graph = [[]for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append((e, 1))

def dijkstra(start):

    dist = [INF] * (n+1)
    dist[start] = 0
    
    q = []
    heappush(q, (0, start))

    while q:
        cost, now = heappop(q)

        if cost > dist[now]:
            continue

        for nxt, new_cost in graph[now]:
            ncost = cost + new_cost

            if ncost < dist[nxt]:
                dist[nxt] = ncost
                heappush(q, (ncost, nxt))
    return dist
    
result = dijkstra(x)

answer = []
for i in range(1, n+1):
    if result[i] == k:
        answer.append(i)

if answer:
    for a in answer:
        print(a)
else:
    print(-1)