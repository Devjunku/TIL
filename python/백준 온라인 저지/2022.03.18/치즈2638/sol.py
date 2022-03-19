from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pan = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    q = deque([])
    q.append((0, 0))

    visited = [[False for _ in range(m)] for _ in range(n)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if not visited[nx][ny] and pan[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                continue
            
            if not visited[nx][ny] and pan[nx][ny] == 1:
                pan[nx][ny] -= 2
                continue
            
            if pan[nx][ny] == -1:
                pan[nx][ny] -= 2

    for i in range(n):
        for j in range(m):
            if pan[i][j] == -3:
                pan[i][j] = 0
            elif pan[i][j] == -1:
                pan[i][j] = 1
                
t = 0
while True:

    toggle = True
    for i in range(n):
        for j in range(m):
            if pan[i][j] == 1:
                toggle = False

    if toggle:
        print(t)
        break

    bfs()
    t += 1
    
