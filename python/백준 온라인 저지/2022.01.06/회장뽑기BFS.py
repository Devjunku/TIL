from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):

    visited = [0 for _ in range(n + 1)]
    q = deque([])
    q.append((start))
    while q:
        node = q.popleft()
        for nxt_node in graph[node]:
            if nxt_node == start:
                continue
            if visited[nxt_node] != 0:
                continue
            visited[nxt_node] += visited[node] + 1
            q.append(nxt_node)

    return visited


n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    s, e = map(int, input().split())
    if s == -1 and e == -1:
        break
    graph[s].append(e)
    graph[e].append(s)

dic = {}

for i in range(1, n+1):
    dic[i] = max(bfs(i))

res = list(sorted(dic.items(), key=lambda x: (x[1])))
mini = res[0][1]

answer = []
for r in res:
    if r[1] == mini:
        answer.append(r)
    else:
        break

print(mini, len(answer))
for a in answer:
    print(a[0], end =" ")