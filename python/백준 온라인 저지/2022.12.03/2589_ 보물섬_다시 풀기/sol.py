from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mapp = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 어디서든 bfs 한 번 진행하면 || 근데 이거 뭔가 트리 같은데..
# 어디서든 한 번 bfs를 돌리고 가장 거리가 멀리 나온 아이만 있으면 될거 같은데
# 그리고 다시 거기서 돌리면 되지 않나...?

# 경계가 나눠져 있는 부분은 봐야할거 같다.
# 어차피 경계는 bfs를 한 번 돌고 끝날 때가 기준이니까.
# 이부분을 좀 기억하면 될거 같다.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):

    Q = deque([(x, y)])

    visited[x][y] = True 

    dist = [[0 for _ in range(m)] for _ in range(n)]
    dist_value = 0
    dist_x = x
    dist_y = y


    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m): continue
            if mapp[nx][ny] == "W": continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            dist[nx][ny] = dist[cx][cy] + 1
            if dist[nx][ny] > dist_value:
                dist_value = max(dist_value, dist[nx][ny])
                dist_x, dist_y = nx, ny
            Q.append((nx, ny))

    return [dist_x, dist_y, dist_value]

# bfs를 한 번 돌 때 기억해야 하는건, 가장 먼 거리 값과 그 끝나는 좌표값을 기억해야 한다.
dist_point = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and mapp[i][j] == "L":
            dist_point.append(bfs(i, j))

visited = [[False for _ in range(m)] for _ in range(n)]

answer = 0
for x, y, d in dist_point:
    rx, ry, rd = bfs(x, y)
    answer = max(answer, rd)

print(answer)