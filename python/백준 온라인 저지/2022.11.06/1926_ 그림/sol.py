import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

num_picture = 0
max_picture = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global max_picture, num_picture
    visited[x][y] = True

    Q = deque([(x, y)])
    cnt = 1

    while Q:
        cx, cy = Q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if not (0 <= nx < N and 0 <= ny < M): continue
            if paper[nx][ny] == 0: continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            cnt += 1
            Q.append((nx, ny))

    num_picture += 1
    max_picture = max(max_picture, cnt)

for i in range(N):
    for j in range(M):
        if paper[i][j] == 0: continue
        if visited[i][j]: continue
        bfs(i, j)
    
print(num_picture)
print(max_picture)