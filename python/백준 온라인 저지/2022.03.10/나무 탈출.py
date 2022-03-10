import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance_sum = 0

for i in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(now, count):
    global distance_sum

    if not visited[now] and len(graph[now]) == 1 and now != 1:
        distance_sum += count
    
    visited[now] = True

    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt, count + 1)

dfs(1, 0)

print("No" if distance_sum % 2 == 0 else "Yes")