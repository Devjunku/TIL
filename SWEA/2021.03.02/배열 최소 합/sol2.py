import sys

sys.stdin = open('sample_input.txt')

def DFS(idx, visited):
    global S, Mini
    if idx >= N:
        if S < Mini:
            Mini = S
            return
    if S > Mini:
        return

    for i in range(N):
        if visited[i] == 0:
            S += arr[idx][i]
            visited[i] = 1
            DFS(idx+1, visited)
            visited[i] = 0
            S -= arr[idx][i]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    visited = [0] * N
    S = 0
    Mini = 99



