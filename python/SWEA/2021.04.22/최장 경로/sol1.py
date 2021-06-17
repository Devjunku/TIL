import sys

sys.stdin = open('sample_input.txt')

def dfs(idx, cnt):
    global res

    visited[idx] = 0

    cnt += 1

    if res < cnt:
        res = cnt
    
    for i in graph[idx]:
        if visited[i]:
            dfs(i, cnt)
    
    visited[idx] = 1

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    if M:
        visited = [1 for _ in range(N+1)]
        info = [list(map(int, input().split())) for _ in range(M)]
        graph = [[] for _ in range(N+1)]
        res = 0

        for i1, i2 in info:
            graph[i1].append(i2)
            graph[i2].append(i1)

        for i in range(N):
            dfs(i, 0)

        print(f'#{t} {res}')

    else:
        print(f'#{t} {1}')