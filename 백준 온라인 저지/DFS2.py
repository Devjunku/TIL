# 인접행렬로 푼 코드 2
def dfs(v): #
    print(v, end = ' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

n, m, v = map(int, input().split())
s = [[0]*(n+1) for i in range(n+1)]

visit = [0 for i in range(n+1)]


for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

dfs(v)