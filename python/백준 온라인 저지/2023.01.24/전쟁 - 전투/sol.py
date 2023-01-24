import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(input().strip()) for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dic = {
    "W": 0,
    "B": 0
}

def dfs(y, x):
    global num

    visited[y][x] = True

    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]

        if not (0 <= nx < N and 0 <= ny < M): continue
        if visited[ny][nx]: continue
        if graph[ny][nx] != target: continue
        num += 1
        dfs(ny, nx)


for i in range(M):
    for j in range(N):
        if visited[i][j]: continue
        target = graph[i][j]
        num = 1
        dfs(i, j)
        dic[target] += num**2

for value in dic.values():
    print(value, end = " ")