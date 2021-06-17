from collections import deque

n, m, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(m)]for _ in range(h)]

print(arr)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dz = [0, -1, 1]

def start(arr):
    point = []
    for k in range(h):
        for i in range(m):
            for j in range(n):
                if arr[k][i][j] == 1:
                    point.append((k, i, j))
    return point

def impossible(arr):
    max_dat = 1
    for k in range(h):
        for i in range(m):
            for j in range(n):
                if arr[k][i][j] == 0:
                    return -1
                elif arr[k][i][j] > max_dat:
                    max_dat = arr[k][i][j]
    return max_dat - 1
            
def safe(z, y, x):
    if z < 0 or z >= h or y < 0 or y >= m or x < 0 or x >= n:
        return False
    elif arr[z][y][x] == -1:
        return False
    else:
        return True
    
def bfs(start):
    queue = deque()
    queue.extend(start)
    while queue:
        z, y, x = queue.popleft()
        for k in range(3):
            for i in range(4):
                nz = z + dz[k]
                ny = y + dy[i]
                nx = x + dx[i]
                if not safe(nz, ny, nx):
                    continue
                else:
                    if arr[nz][ny][nx] == 0:
                        arr[nz][ny][nx] = arr[z][y][x] + 1
                        queue.append((nz, ny, nx))
                    elif arr[nz][ny][nx] > arr[z][y][x] + 1:
                        arr[nz][ny][nx] = arr[z][y][x] + 1
                        queue.append((nz, ny, nx))
    return impossible(arr)
print(bfs(start(arr)))