import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [ [] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

def dijkstra(start):

    INF = int(1e9)
    dist = [INF] * (n+1)
    nodes = [[] for _ in range(n+1)]
    pq = []
    dist[start] = 0
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        if weight > dist[now]: continue

        for nxt, cost in graph[now]:
            new_cost = cost + weight

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heappush(pq, (new_cost, nxt))
                nodes[nxt].append(now)
    
    return nodes

answer = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    data = dijkstra(i+1)
    for j in range(n):
        if data[j+1]:
            answer[j][i] = data[j+1][-1]
        else:
            answer[j][i] = "-"

for i in range(n):
    print(*answer[i])