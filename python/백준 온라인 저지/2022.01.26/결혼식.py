import sys
from collections import deque
input = sys.stdin.readline

node_num = int(input())
list_num = int(input())

graph = [[] for _ in range(node_num)]

for _ in range(list_num):
    s, e = map(int, input().split())
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

def bfs():

    q = deque([])
    visited = [-1 for _ in range(node_num)]
    visited[0] = 1
    q.append((0, 1))

    while q:
        node, relation = q.popleft()
        for nxt in graph[node]:
            if visited[nxt] == -1:
                visited[nxt] = relation + 1
                q.append((nxt, relation+1))
    
    return visited

result = bfs()
cnt = 0
for r in result:
    if 1 < r < 4:
        cnt += 1

print(cnt)

