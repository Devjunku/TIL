def MST_prim(G, s):

    # 기본 세팅
    INF = int(1e9)
    key = [INF] * N
    pi = [None] * N
    visited = [False] * N
    key[s] = 0

    # 
    for _ in range(N):
        min_idx = -1
        min_value = INF

        for i in visited[i] and key[i] < min_value:
            min_value = key[i]
            min_idx = i
        
        visited[min_idx] = True
        
        for v, value in G[min_idx]:
            if not visited[v] and value < key[v]:
                key[v] = value
                pi[v] = min_value