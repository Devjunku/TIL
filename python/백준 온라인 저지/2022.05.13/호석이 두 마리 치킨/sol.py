from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append((e, 1))
    graph[e].append((s, 1))

def dijkstra(chik1, chik2):
    INF = int(10e9)
    dist = [INF] * (n+1)
    dist[chik1] = 0
    dist[chik2] = 0

    pq = []
    heappush(pq, (0, chik1))
    heappush(pq, (0, chik2))

    while pq:
        cost, node = heappop(pq)

        if dist[node] < cost: continue

        for nxt, w in graph[node]:
            n_c = cost + w

            if n_c < dist[nxt]:
                dist[nxt] = n_c
                heappush(pq, (n_c, nxt))

    for i in range(1, n+1):
        dist[i] = dist[i]*2

    return dist

answer = [0, 0, int(10e9)]
for i in range(1, n+1):
    for j in range(i+1, n+1):
        s = sum(dijkstra(i, j)[1:])
        if answer[2] > s:
            answer[0] = i
            answer[1] = j
            answer[2] = s
    
print(*answer)