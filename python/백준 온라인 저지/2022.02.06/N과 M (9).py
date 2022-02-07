import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []
visited = [False for i in range(n)]
def dfs(a, num):

    if num == m:
        if " ".join(map(str, a)) in res:
            return
        else:
            res.append(" ".join(map(str, a)))
        return
    
    for i in range(n):
        if visited[i]:
            continue
        a.append(arr[i])
        visited[i] = True
        dfs(a, num+1)
        a.pop()
        visited[i] = False

dfs([], 0)

for r in res:
    print(r)