def DFS(idx, visited):
    global S, Mini
    if idx >= 5:
        if S < Mini:
            Mini = S
            return
    if S > Mini:
        return

    for i in range(5):
        if visited[i] == 0:
            S += arr[idx][i]
            visited[i] = 1
            DFS(idx+1, visited)
            visited[i] = 0
            S -= arr[idx][i]


arr = [[5, 2, 1, 1, 9],
       [3, 3, 8, 3, 1],
       [9, 2, 8, 8, 6],
       [1, 5, 7, 8, 3],
       [5, 5, 4, 6, 8]]

visited = [0] * 5
S = 0
Mini = 99
DFS(0, visited)
print(Mini)