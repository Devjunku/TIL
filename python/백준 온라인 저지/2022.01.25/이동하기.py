import sys

input = sys.stdin.readline

n, m = map(int, input().split())
zero_arr = [0 for _ in range(m+1)]

arr = [zero_arr]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] += max(arr[i-1][j], arr[i][j-1])

print(arr[n][m])