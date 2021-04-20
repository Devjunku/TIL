N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

def dfs():
    global arr1, visited, cnt, dx, dy
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                visited[i][j] = 0
                cnt += 1
                stack = []
                stack.append((i, j))
                while stack:
                    # print(stack)
                    x, y = stack.pop()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if not safe(nx, ny):
                            continue
                        if visited[nx][ny] == 1:
                            stack.append((nx, ny))
                            visited[nx][ny] = 0

def safe(x, y):
    global arr1
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

dx = [0, 0, 1 ,-1]
dy = [1, -1, 0, 0]

max_v = arr[0][0]
min_v = arr[0][0]
for i in range(N): # 최대 최소 높이 구하기
    for j in range(N):
        if max_v < arr[i][j]:
            max_v = arr[i][j]
        if min_v > arr[i][j]:
            min_v = arr[i][j]

res = 0
for i in range(min_v, max_v+1):
    arr1 = [[0 for _ in range(N)] for _ in range(N)] # 복제
    visited = [[0 for _ in range(N)] for _ in range(N)] # 복제
    for j in range(N):
        for k in range(N):
            if arr[j][k] <= i:
                arr1[j][k] = 0
                visited[j][k] = 0
            else:
                arr1[j][k] = arr[j][k]
                visited[j][k] = 1
    # print(arr1)
    cnt = 0
    dfs()
    # print(cnt)
    if res < cnt:
        res = cnt

print(res)



            





