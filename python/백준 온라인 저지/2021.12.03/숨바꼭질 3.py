from heapq import heappop, heappush

n, k = map(int, input().split())
node = [[] for _ in range(1000002)]

for i in range(100001):
    if i <= 50000:
        node[i].append((2*i, 0))
    node[i].append((i-1, 1))
    node[i].append((i+1, 1))
    

def dijkstra(s, e, node):
    INF = 100000
    dist = [INF for _ in range(1000002)]
    dist[s] = 0

    q = []
    heappush(q, (0, s))

    while q:
        distance, now = heappop(q)

        if dist[now] < distance:
            continue

        for nxt, dis in node[now]:
            cost = dis + distance

            if cost < dist[nxt]:
                dist[nxt] = cost
                heappush(q, (cost, nxt))
    return dist[e]

print(dijkstra(n, k, node))