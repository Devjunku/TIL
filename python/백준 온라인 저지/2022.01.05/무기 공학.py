n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def rightup(y, x):
    return arr[y][x-1] + arr[y+1][x] + arr[y][x] * 2

def rightdown(y, x):
    return arr[y-1][x] + arr[y][x-1] + arr[y][x] * 2

def leftup(y, x):
    return arr[y][x+1] + arr[y+1][x] + arr[y][x] * 2

def leftdown(y, x):
    return arr[y-1][x] + arr[y][x+1] + arr[y][x] * 2

ans = 0

def dfs(y, x, cumsum):
    global ans

    if x == m:
        x = 0
        y += 1
    
    if y == n:
        ans = max(ans, cumsum)
        return
    
    if not visited[y][x]:
        if y + 1 < n and x - 1 >= 0 and not visited[y+1][x] and not visited[y][x-1]:
            visited[y][x] = True
            visited[y+1][x] = True
            visited[y][x-1] = True
            dfs(y, x+1, rightup(y, x) + cumsum)
            visited[y][x] = False
            visited[y+1][x] = False
            visited[y][x-1] = False

        if y - 1 >= 0 and x - 1 >= 0 and not visited[y-1][x] and not visited[y][x-1]:
            visited[y][x] = True
            visited[y-1][x] = True
            visited[y][x-1] = True
            dfs(y, x+1, rightdown(y, x) + cumsum)
            visited[y][x] = False
            visited[y-1][x] = False
            visited[y][x-1] = False

        if y + 1 < n and x + 1 < m and not visited[y+1][x] and not visited[y][x+1]:
            visited[y][x] = True
            visited[y+1][x] = True
            visited[y][x+1] = True
            dfs(y, x+1, leftup(y, x) + cumsum)
            visited[y][x] = False
            visited[y+1][x] = False
            visited[y][x+1] = False
        
        if y - 1 >= 0 and x + 1 < m  and not visited[y-1][x] and not visited[y][x+1]:
            visited[y][x] = True
            visited[y-1][x] = True
            visited[y][x+1] = True
            dfs(y, x+1, leftdown(y, x) + cumsum)
            visited[y][x] = False
            visited[y-1][x] = False
            visited[y][x+1] = False
    
    dfs(y, x+1, cumsum)


dfs(0, 0, 0)
print(ans)