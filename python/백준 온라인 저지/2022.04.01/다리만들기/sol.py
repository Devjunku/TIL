from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

count = 1
answer = int(1e9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    global count
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    arr[x][y] = count

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny] or arr[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            arr[nx][ny] = count
            q.append((nx, ny))

def bridge(z):
    global answer
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == z:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if arr[nx][ny] > 0 and arr[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return

            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))



for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            bfs(i, j)
            count += 1

for i in range(1, count):
    bridge(i)

print(answer)