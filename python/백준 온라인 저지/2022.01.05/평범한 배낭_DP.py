import sys

n, k = map(int, sys.stdin.readline().strip().split())

init = [[0, 0]]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    init.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = init[i][0]
        v = init[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])

print(knapsack[n][k])