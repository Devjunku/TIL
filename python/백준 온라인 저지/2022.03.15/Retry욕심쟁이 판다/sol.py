from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

woods = [list(map(int, input().split())) for _ in range(n)]
visited = [[1 for _ in range(n)] for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        q = deque([(i, j, 1)])
        while q:
            x, y, turn = q.popleft()
            answer = max(answer, turn)
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if woods[x][y] >= woods[nx][ny]:
                        continue
                    visited[nx][ny] = max(turn + 1, visited[nx][ny])
                    q.append((nx, ny, visited[nx][ny]))

print(answer)