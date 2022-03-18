import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, L, R = map(int, input().split())

populations = [list(map(int, input().split())) for _ in range(n)]


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

point = []

def dfs(x, y, p_num, num):
    global cnt, popul
    point.append((x, y))
    cnt += 1
    popul += populations[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n): continue
        if visited[nx][ny]: continue
        difference = abs(populations[nx][ny] - populations[x][y])
        if L <= difference <= R:
            visited[nx][ny] = True
            dfs(nx, ny, p_num+populations[nx][ny], num+1)

def is_go_to_another(populations):
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if not (0 <= nx < n and 0 <= ny < n): continue
                difference = abs(populations[nx][ny] - populations[i][j])
                if L <= difference <= R:
                    return True
    return False

count = 0

while True:
    if is_go_to_another(populations):
        visited = [[False for _ in range(n)] for _ in range(n)]
        count += 1
        for i in range(n):
            for j in range(n):
                if visited[i][j]: continue
                visited[i][j] = True
                point = []
                cnt = 0
                popul = 0
                dfs(i, j, populations[i][j], 1)
                for p in point:
                    populations[p[0]][p[1]] = int(popul/cnt)
    else:
        print(count)
        break