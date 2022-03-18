import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())

algo_spot = [list(input().strip()) for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def go_to_nm():

    pq = []
    heappush(pq, (0, 0, 0))
    visited = [[-1 for _ in range(n)] for _ in range(m)]
    visited[0][0] = 0

    while pq:
        cost, x, y = heappop(pq)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < m and 0 <= ny < n):
                continue

            if visited[nx][ny] != -1:
                continue

            if algo_spot[nx][ny] == "1":
                visited[nx][ny] = cost + 1
                heappush(pq, (cost+1, nx, ny))
            else:
                visited[nx][ny] = cost
                heappush(pq, (cost, nx, ny))

        if visited[m-1][n-1] != -1:
            return visited

res = go_to_nm()
print(res[m-1][n-1])