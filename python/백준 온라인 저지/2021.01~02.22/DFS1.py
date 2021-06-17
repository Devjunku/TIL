# 인접 행렬로 푼 코드 1

from sys import stdin

def dfs(adj, V, hist):
    hist.append(V)
    for i in range(1, N+1):
        if adj[V][i] and i not in hist:
            hist = dfs(adj, i, hist)
    return hist
    


N, M, V = map(int,stdin.readline().rstrip().split())

adj = [[0] * (N+1) for _ in range(N+1)]
for m in range(M):
    s, e = map(int,stdin.readline().rstrip().split())
    adj[s][e] = 1
    adj[e][s] = 1

print(adj)

print(dfs(adj, V, []))

    


