from sys import stdin

N = int(stdin.readline().rstrip())

arr = []
for _ in range(N):
    arr.append(list(map(int, stdin.readline().rstrip().split())))

print(arr)
level = []
idx = list(range(0, N))
for i in range(N):
    cnt  = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    level.append(cnt)

print(*level)
        
