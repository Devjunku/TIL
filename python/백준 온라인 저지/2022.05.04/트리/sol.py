import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
del_node = int(input())
del_node_s = set()
del_node_s.add(del_node)


graph = [[] for _ in range(n)]

for i in range(len(p)):
    if p[i] == -1: continue
    graph[p[i]].append(i)

def del_tree(start):
    global graph

    for nxt in graph[start]:
        del_tree(nxt)
    graph[start].clear()
    return

del_tree(del_node)

visited = [False for _ in range(n+1)]
cnt = 0

def curcuit_tree(start):
    global cnt
    if not graph[start]:
        cnt += 1
        return

    for nxt in graph[start]:
        if not visited[nxt] and nxt not in del_node_s:
            visited[nxt] = True
            curcuit_tree(nxt)

for i in range(n):
    if not visited[i] and graph[i]:
        visited[i] = True
        curcuit_tree(i)

print(cnt)