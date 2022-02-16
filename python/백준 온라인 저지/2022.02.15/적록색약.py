import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def normal_bfs(x, y):

    q = deque([])
    q.append((x, y, arr[x][y]))
    normal_visited[x][y] = True

    while q:
        cx, cy, color = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if color == arr[nx][ny] and not normal_visited[nx][ny]:
                    q.append((nx, ny, arr[nx][ny]))
                    normal_visited[nx][ny] = True

def abnormal_bfs(x, y):

    q = deque([])
    q.append((x, y, arr[x][y]))
    abnormal_visited[x][y] = True

    while q:
        cx, cy, color = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if color in ["G", "R"] and arr[nx][ny] in ["G", "R"] and not abnormal_visited[nx][ny]:
                    q.append((nx, ny, arr[nx][ny]))
                    abnormal_visited[nx][ny] = True
                elif color == "B" and arr[nx][ny] =="B" and not abnormal_visited[nx][ny]:
                    q.append((nx, ny, arr[nx][ny]))
                    abnormal_visited[nx][ny] = True

normal_visited = [[False for _ in range(n)] for _ in range(n)]
abnormal_visited = [[False for _ in range(n)] for _ in range(n)]
normal_district = 0
abnormal_district = 0
for i in range(n):
    for j in range(n):
        if not normal_visited[i][j]:
            normal_bfs(i, j)
            normal_district += 1
        if not abnormal_visited[i][j]:
            abnormal_bfs(i, j)
            abnormal_district += 1

print(f"{normal_district} {abnormal_district}")