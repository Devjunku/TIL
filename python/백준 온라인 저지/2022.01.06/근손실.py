n, k = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False for _ in range(n)]

cnt = 0

def dfs(day, weight):
    global cnt

    if weight < 500:
        return
    
    if day == n:
        cnt += 1
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(day+1, weight+arr[i]-k)
            visited[i] = False

dfs(0, 500)
print(cnt)
