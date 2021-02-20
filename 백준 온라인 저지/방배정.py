from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())

arr = [[0 for _ in range(6)] for _ in range(2)]

for _ in range(N):
    s, l = map(int, stdin.readline().rstrip().split())
    arr[s][l-1] += 1

cnt = 0
for i in range(2):
    for j in range(6):
        if arr[i][j] == 0:
            continue
        else:
            if arr[i][j] % K == 0:
                cnt += arr[i][j] // K
            else:
                cnt += (arr[i][j] // K) + 1
print(cnt)         