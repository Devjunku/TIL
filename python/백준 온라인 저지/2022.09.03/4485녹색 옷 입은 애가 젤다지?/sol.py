import sys
from heapq import heappop, heappush
input = sys.stdin.readline

number = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra(graph, n, cave):

    INF = int(1e9)

    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = cave[0][0]
    q = []
    heappush(q, (0, 0, cave[0][0]))

    while q:

        x, y, cost = heappop(q)

        if cost > distance[x][y]: continue

        for i, j in graph[x][y]:
            _cost = cost + cave[i][j]

            if _cost < distance[i][j]:
                distance[i][j] = _cost
                heappush(q, (i, j, _cost))

    return distance[n-1][n-1]


while True:

    n = int(input())

    if not n: break

    cave = [list(map(int, input().split())) for _ in range(n)]
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                x, y = i - dx[k], j - dy[k]
                if not (0 <= x < n and 0 <= y < n):continue
                graph[i][j].append((x, y))
    
    print(f"Problem {number}: {dijkstra(graph, n, cave)}")
    number += 1