import sys

sys.stdin = open('sample_input.txt')


def DFS(idx, visited):
    global Min, s
    if idx >= N:
        if s < Min:
            Min = s
        return

    if s > Min:
        return

    for i in range(0,N):
        if visited[i] == 0:
            s += arr[idx][i]
            visited[i] = 1
            DFS(idx+1, visited)
            visited[i] = 0
            s -= arr[idx][i]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))


    visited = [0] * N
    s = 0
    Min = 999

    DFS(0, visited)

    print('#{} {}'.format(t, Min))





