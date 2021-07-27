N, M, K, X = map(int, input().split())
graph = [ [] for _ in range(N + 1)]

for _ in range(4):
    s, e = map(int, input().split())
    graph[s].append(e)


