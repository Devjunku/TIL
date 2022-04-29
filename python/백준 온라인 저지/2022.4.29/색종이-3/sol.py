import sys
input = sys.stdin.readline


arr = [[0 for _ in range(102)] for _ in range(102)]

n = int(input())

for _ in range(n):
    c, r = map(int, input().split())
    for i in range(r , r+10):
        for j in range(c, c+10):
            arr[i][j] = 1

for i in range(1, 102):
    for j in range(1, 102):
        if arr[i][j] == 0: continue
        arr[i][j]+= arr[i][j-1]

for i in range(1, 102):
    for j in range(1, 102):
        if arr[j][i] == 0: continue
        arr[j][i] += arr[j-1][i]

mv = 0
for i in range(102):
    mv = max([mv] + arr[i])

print(mv)


