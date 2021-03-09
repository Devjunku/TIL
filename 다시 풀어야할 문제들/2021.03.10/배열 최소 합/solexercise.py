import sys

sys.stdin = open('sample_input.txt')

def dfs(idx, visited):
    global Min, S

    if idx >= N:
        if S < Min:
            Min = S
        return
        
    if S > Min:

        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            S += maze[idx][i]
            dfs(idx+1, visited)
            visited[i] = 0
            S -= maze[idx][i]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input().split())))
    
    S = 0
    Min = 99
    visited = [0] * N

    dfs(0, visited)

    print(Min)

