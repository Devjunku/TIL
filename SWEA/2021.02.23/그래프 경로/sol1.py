import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# 재귀함수를 이용

def dfs(graph, v, visited):
    visited[v] = True

    # print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def DFS(graph, s, V):
    visited = [False] * V
    dfs(graph, s, visited)
    return visited

for t in range(1, T+1):

    V, E = map(int, input().split())

    adj = [ [] for _ in range(V)] # 인접 리스트 만들기

    for _ in range(E):
        SN, EN = map(int, input().split())
        adj[SN-1].append(EN-1)


    S, G = map(int, input().split())

    if DFS(adj, S-1, V)[G-1] == True:
        print('#{} {}'.format(t, 1))
    else:
        print('#{} {}'.format(t, 0))

# 반복구문을 활용한

def DFS(graph, s):
    stack = [s]
    visited = []

    while stack:
        u = stack.pop()
        visited.append(u)
        for v in graph[u]:
            if v not in visited + stack:
                stack.append(v)

    return visited