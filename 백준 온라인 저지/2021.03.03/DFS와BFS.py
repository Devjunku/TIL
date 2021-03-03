import sys

sys.stdin = open('dfs_bfs_input.txt')

def dfs(graph, v):
    stack = [v]
    visited = []
    while stack:
        w = stack.pop()
        if w not in visited:
            visited.append(w)
            for i in range(len(graph[w])-1, -1, -1):
                stack.append(graph[w][i])
    return visited

def bfs(graph, v):
    queue = [v]
    visited = []
    while queue:
        v = queue.pop(0)
        visited.append(v)
        queue1 = []
        for w in graph[v]:
            if w not in visited:
                queue1.append(w)
        if queue1:
            queue1 = sorted(queue1, reverse = False)
            for _ in range(len(queue1)):
                queue.append(queue1.pop(0))

    return visited



T = int(input())
for t in range(1, T+1):
    n, m, v = map(int, input().split())

    graph = [ [] for _ in range(n+1)]

    for _ in range(m):
        si, ei = map(int, input().split())
        graph[si].append(ei)
        graph[ei].append(si)
    
    for i in range(len(graph)):
        graph[i].sort()
    print(graph)
    
    print(dfs(graph, v))
    print(bfs(graph, v))
