import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

array = [ [ list(map(int, input().split())) for _ in range(N) ] for _ in range(H) ]

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(x, y, z, d):
    array[z][y][x] = -2
    q = deque([(x, y, z, d)])

    days = d

    while q:
        cx, cy, cz, d = q.popleft()
        if days < d:
            days = d
        for i in range(6):
            nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
            if 0 <= nx < M and  0 <= ny < N and 0 <= nz < H:
                if array[nz][ny][nx] == 0:
                    array[nz][ny][nx] = -2
                    q.append((nx, ny, nz, d+1))
    return days

min_day = 0
for m in range(M):
    for n in range(N):
        for h in range(H):
            if array[h][n][m] == 1:
                days = bfs(m, n, h, 0)
                if min_day < days:
                    min_day = days

res = 0
for m in range(M):
    for n in range(N):
        for h in range(H):
            if array[h][n][m] == 0:
                res = -1
                break
        if res == -1:
            break
    if res == -1:
        break

if res == -1: print(res)
else: print(min_day)