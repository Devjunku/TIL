import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

def dfs(x, y):
    global answer, dp

    if dp[x][y] != -1: return dp[x][y]

    tmp = 0
    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n): continue
        if arr[nx][ny] > arr[x][y]: tmp = max(tmp, dfs(nx, ny))
    
    dp[x][y] += tmp

    if answer < dp[x][y]: answer = dp[x][y]

    return dp[x][y]

for i in range(n):
    for j in range(n):
        dfs(i, j)

print(answer)



