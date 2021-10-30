from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(s):

    distance = [INF] * (N+1)
    distance[s] = 0
    h = []
    heappush(h, (0, s))

    while h:
        dist, now = heappop(h)

        if distance[now] < dist:
            continue

        for nxt, time in graph[now]:
            cost = dist + time

            if cost < distance[nxt]:
                distance[nxt] = cost
                heappush(h, (cost, nxt))
    
    return distance

max_value = 0
back = dijkstra(X)
for i in range(1, N+1):
    go = dijkstra(i)
    max_value = max(max_value, go[X] + back[i])

print(max_value)