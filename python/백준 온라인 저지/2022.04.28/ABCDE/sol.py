import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

answer = 0
def friend(now, num):
    global answer

    if num >= 4:
        answer = 1
        return

    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            friend(nxt, num+1)
            visited[nxt] = False

visited = [0 for _ in range(n+1)]
for i in range(n):
    if answer: break
    visited[i] = True
    friend(i, 0)
    visited[i] = False

print(answer)