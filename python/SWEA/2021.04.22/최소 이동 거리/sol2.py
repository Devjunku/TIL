import sys

sys.stdin = open('sample_input.txt')

import heapq

def dijkstra():
    global dist

    q = []
    heapq.heappush(q, (0, 0))

    while q:

        distance, idx = heapq.heappop(q)

        if vistied[idx]:
            continue
        
        vistied[idx] = 1

        for a, b in node[idx]:
            if dist[a] > distance + b:
                dist[a] = distance + b
                heapq.heappush(q, (dist[a], a))


INF = int(1e9)

T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())

    dist = [INF] * (N+1)
    dist[0] = 0
    node = [[] for _ in range(N+1)]
    vistied = [0 for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        node[s].append((e, w))

    dijkstra()
        
    print(f'#{t} {dist[N]}')

