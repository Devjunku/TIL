from collections import deque

n, m  = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def safe(y, x):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    elif arr[y][x] == -1:
        return False
    return True

def impossible(arr):
    max_dat = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                return -1
            elif arr[i][j] > max_dat:
                max_dat = arr[i][j]
    return max_dat-1

def start_point(arr):
    point = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                point.append((i, j))
    return point

def bfs(start):
    global arr
    queue = deque()
    queue.extend(start)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not safe(ny, nx):
                continue
            else:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = arr[y][x] + 1
                    queue.append((ny, nx))
                elif arr[y][x] + 1 < arr[ny][nx]:
                    arr[ny][nx] = arr[y][x] + 1
                    queue.append((ny, nx))
    return impossible(arr)

print(bfs(start_point(arr)))


    


