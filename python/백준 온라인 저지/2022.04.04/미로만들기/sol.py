from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())

maze = [list(map(int, list(input().strip()))) for _ in range(n)]
INF = int(1e9)
INF_ARR = [[INF for _ in range(n)] for _ in range(n)]

pq = [(0, 0, 0)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while pq:
    cost, x, y = heappop(pq)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if maze[nx][ny] == 0 and cost+1 < INF_ARR[nx][ny]:
            INF_ARR[nx][ny] = cost+1
            heappush(pq, (cost+1, nx, ny))
        elif maze[nx][ny] == 1 and INF_ARR[nx][ny] == INF:
            INF_ARR[nx][ny] = cost
            heappush(pq, (cost, nx, ny))

print(INF_ARR[n-1][n-1])