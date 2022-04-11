import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, r, q = map(int, input().split())

graph  = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

size = [0]*(n+1)

def count_subtree_nodes(cur):
    visited[cur] = True
    size[cur] = 1
    for node in graph[cur]:
        if not visited[node]:
            count_subtree_nodes(node)
            size[cur] += size[node]

count_subtree_nodes(r)

for _ in range(q):
    print(size[int(input())])