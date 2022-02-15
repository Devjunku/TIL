import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
cost = int(1e9)

def dfs(num, cnt):
    global cost

    if num == 3:
        cost = min(cnt, cost)
        return
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            if not visited[i][j] and not visited[i-1][j] and not visited[i][j-1] and not visited[i+1][j] and not visited[i][j+1]:
                visited[i][j], visited[i-1][j], visited[i][j-1], visited[i+1][j], visited[i][j+1] = True, True, True, True, True
                dfs(num+1, cnt + arr[i][j] + arr[i-1][j] + arr[i][j-1] + arr[i+1][j] + arr[i][j+1])
                visited[i][j], visited[i-1][j], visited[i][j-1], visited[i+1][j], visited[i][j+1] = False, False, False, False, False

dfs(0, 0)
print(cost)