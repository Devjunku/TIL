import sys

sys.stdin = open('input.txt')

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

for t in range(1, 11):
    TC, N = map(int, input().split())

    data = list(map(int, input().split()))

    adj_list = [[] for _ in range(101)]
    for i in range(N):
        adj_list[data[2*i]].append(data[2*i+1])

    if 99 in DFS(adj_list, 0):
        print('#{} {}'.format(TC, 1))
    else:
        print('#{} {}'.format(TC, 0))