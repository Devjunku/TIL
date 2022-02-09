import sys
sys.setrecursionlimit(100000) 
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] = -1


def dfs(x, y):
    global cnt
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and arr[nx][ny] != -1:
                visited[nx][ny] = True
                cnt += 1
                dfs(nx, ny)


answer = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != -1 and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            answer.append(cnt)

answer.sort()
print(len(answer))
print(*answer)