import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
connect = [[] for _ in range(n)]

for i in range(n):
    x, y, d, g = data[i]
    connect[i].append(d)
    for _ in range(g):
        reverse = list(reversed(connect[i]))
        for j in reverse:
            connect[i].append((j+1)%4)

arr = [[False] * 101 for _ in range(101)]
for i in range(n):
    x, y, d, g = data[i]
    arr[y][x] = True
    for j in connect[i]:
        x, y = x + dx[j], y + dy[j]
        if  0 <= x <= 100 and 0 <= y <= 100:
            arr[y][x] = True

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            cnt += 1

print(cnt)