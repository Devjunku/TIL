import sys

n, m = map(int, input().split())

arr = [[0] * (n + 1)]
for _ in range(n):
    arr.append([0]+list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n):
        arr[i][j+1] += arr[i][j]

for j in range(1, n+1):
    for i in range(1, n):
        arr[i+1][j] += arr[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])