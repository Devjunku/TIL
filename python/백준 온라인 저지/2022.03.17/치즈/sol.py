import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

mapping = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(mapping):

    q = deque([])
    q.append((0,0))

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if not visited[nx][ny] and mapping[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
            elif not visited[nx][ny] and mapping[nx][ny] == 1:
                mapping[nx][ny] = -1
                visited[nx][ny] = True
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mapping[i][j] == -1:
                mapping[i][j] = 0
            elif mapping[i][j] == 1:
                cnt += 1
    
    return mapping, cnt

count = 0
cheese = 0

for i in range(n):
    for j in range(m):
        if mapping[i][j] == 1:
            cheese += 1

while True:
    mapping, cnt = bfs(mapping)
    count += 1
    if cnt == 0:
        print(count)
        print(cheese)
        break
    else:
        cheese = cnt