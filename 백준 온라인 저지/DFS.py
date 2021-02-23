# 인접리스트로 푼 풀이 연습장
# https://underflow101.tistory.com/10 참고
from sys import stdin

n, m, v = map(int, stdin.readline().rstrip().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, stdin.readline().rstrip().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(len(adj)):
    adj[i].sort()

def DFS(adj, v):
    stack = [v]
    visited = []
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.append(u)
            if adj[u] == None:
                return visited
            for i in range(len(adj[u])-1, -1, -1):
                stack.append(adj[u][i])
    return visited

for i in DFS(adj, v):
    print(i, end = ' ')
    