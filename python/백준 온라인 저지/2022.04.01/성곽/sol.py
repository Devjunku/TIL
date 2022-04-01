from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
c = [[0 for _ in range(n)]  for _ in range(m)]
q = deque()


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = [1, 2, 4, 8]

def bfs(x, y, cnt):
    q.append((x, y))
    c[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < m and 0 <= ny < n):
                continue

            if d[i] & ~arr[nx][ny] and c[nx][ny] == 0:
                c[nx][ny] = cnt
                q.append((nx, ny))

cnt = 1
for i in range(m):
    for j in range(n):
        if c[i][j] == 0:
            bfs(i, j, cnt)
            cnt += 1

print(cnt - 1)

ans = [0 for _ in range(cnt - 1)]

for i in range(m):
    for j in range(n):
        ans[c[i][j] - 1] += 1

print(max(ans))

max_room = 0
for i in range(m):
    for j in range(n):
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if not (0 <= ni < m and 0 <= nj < n):
                continue

            if c[i][j] != c[ni][nj]:
                room = ans[c[i][j]-1] + ans[c[ni][nj]-1]
                max_room = max(room, max_room)

print(max_room)
