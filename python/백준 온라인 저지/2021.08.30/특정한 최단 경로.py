import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

node1, node2 = map(int, input().split())

def dijkstra(s, e):
    INF = int(1e9)
    distance = [INF] * (N+1)
    distance[s] = 0

    heap = []
    heappush(heap, (0, s))

    while heap:
        dist, now = heappop(heap)

        if dist > distance[now]:
            continue

        for nxt, dis in graph[now]:
            cost = dist + dis

            if cost < distance[nxt]:
                distance[nxt] = cost
                heappush(heap, (cost, nxt))
    
    return distance[e]


if dijkstra(1, N) == int(1e9):
    print(-1)
else:
    answer = min(dijkstra(1, node1) + dijkstra(node1, node2) + dijkstra(node2, N), dijkstra(1, node2) + dijkstra(node2, node1) + dijkstra(node1, N))
    print(answer)