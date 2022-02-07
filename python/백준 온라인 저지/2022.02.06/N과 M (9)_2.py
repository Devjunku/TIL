import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False for i in range(n)]

res = []

def dfs(num):

    if num == m:
        print(" ".join(map(str, res)))
        return
    
    ol = 0

    for i in range(n):
        if not visited[i] and ol != arr[i]:
            visited[i] = True
            res.append(arr[i])
            ol = arr[i]
            dfs(num+1)
            visited[i] = False
            res.pop()
            
dfs(0)