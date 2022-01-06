import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


shark_point = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            shark_point.append((i, j))
    
ans = 0

for i in range(n):
    for j in range(m):

        if arr[i][j] == 1:
            continue

        minimum = int(1e9)
        for shark in shark_point:
            x_interval = abs(i-shark[0])
            y_interval = abs(j-shark[1])
            cnt = 0
            while x_interval != 0 and y_interval != 0:
                cnt += 1
                x_interval -= 1
                y_interval -= 1
            
            cnt += x_interval + y_interval
            minimum = min(minimum, cnt)

        ans = max(ans, minimum)

print(ans)




