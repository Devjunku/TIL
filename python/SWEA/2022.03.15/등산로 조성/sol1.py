import sys

sys.stdin = open('sample_input.txt')

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, num, wise):
    global visited, answer

    if answer <= visited[x][y]:
        answer = visited[x][y]
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and road[nx][ny] < road[x][y]:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, num, wise)
                visited[nx][ny] = 0
            elif visited[nx][ny] == 0 and road[nx][ny] >= road[x][y] and not wise:
                if num - (abs(road[x][y] - road[nx][ny]) + 1) >= 0:
                    visited[nx][ny] = visited[x][y] + 1
                    old = road[nx][ny]
                    road[nx][ny] -= (abs(road[nx][ny] - road[x][y]) + 1)
                    dfs(nx, ny, num - (abs(road[nx][ny] - road[x][y]) + 1), True)
                    road[nx][ny] = old
                    visited[nx][ny] = 0

            
T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    r = [list(map(int, input().split())) for _ in range(n)]
    answer = 1
    m = 0
    for i in range(n):
        m = max([m] + r[i])
    start_xy = []
    for i in range(n):
        for j in range(n):
            if r[i][j] == m:
                start_xy.append((i, j))

    for element in start_xy:
        x, y = element
        road = r[::]
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[x][y] = 1
        dfs(x, y, k, False)

    print(f"#{t} {answer}")