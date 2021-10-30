import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**10)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [ False for _ in range(n+1) ]

def dfs(s):
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(i)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)