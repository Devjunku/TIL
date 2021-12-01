from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny <n:
                if not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

final_cnt = 0
for i in range(1, 101):
    repeat_cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if arr[j][k] < i:
                visited[j][k] = True
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                repeat_cnt += 1
                bfs(i, j)
    
    if repeat_cnt > final_cnt:
        final_cnt = repeat_cnt
    
print(final_cnt)