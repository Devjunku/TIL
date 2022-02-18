import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
sand_init = [list(input().strip()) for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
dx = [1, 0, -1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

q  = deque([])
for i in range(h):
    for j in range(w):
        if sand_init[i][j] == ".":
            sand_init[i][j] = 0
            q.append((i, j))
        else:
            sand_init[i][j] = int(sand_init[i][j])

answer = 0

while q:
    x, y = q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if sand_init[nx][ny] != 0:
                sand_init[nx][ny] -= 1
                if sand_init[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    answer = max(answer, visited[nx][ny])
                    q.append((nx, ny))
    
print(answer)