import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    node_info = list(map(int, input().split()))
    node1 = node_info[0]
    info = node_info[1:-1]
    for i in range(0, len(info), 2):
        graph[node1].append((info[i], info[i+1]))

visited = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
def dfs(s):
    visited[s] = 1
    for info in graph[s]:
        nxt_node, cost = info
        if not visited[nxt_node]:
            distance[nxt_node] = cost + distance[s]
            dfs(nxt_node)
dfs(1)
idx = distance.index(max(distance))
visited = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
dfs(idx)
print(max(distance))