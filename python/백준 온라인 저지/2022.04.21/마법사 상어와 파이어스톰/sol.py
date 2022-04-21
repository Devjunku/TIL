from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
visited = [[False for _ in range(2**n)] for _ in range(2**n)]

orders = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate_90(a, b, c, d):
    init = []
    for i in range(a, c):
        init.append(arr[i][b:d])
    rotate_tuple = zip(*init[::-1])
    rotate_list = [list(elem) for elem in rotate_tuple]

    for i in range(a, c):
        for j in range(b, d):
            arr[i][j] = rotate_list[i-a][j-b]
    

def divide_pan(sx, sy, ex, ey, order):

    if abs(sx-ex) == 2 ** order and abs(sy-ey) == 2 ** order:
        rotate_90(sx, sy, ex, ey)
        return
    
    divide_pan(sx, sy, (sx+ex)//2, (sy+ey)//2, order)
    divide_pan(sx, (sy+ey)//2, (sx+ex)//2, ey, order)
    divide_pan((sx+ex)//2, sy, ex, (sy+ey)//2, order)
    divide_pan((sx+ex)//2, (sy+ey)//2, ex, ey, order)

def bfs(arr, sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0 <= nx < 2**n and 0 <= ny < 2**n):
                continue

            if not visited[nx][ny] and arr[nx][ny] != 0:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt +=1
    return cnt


for order in orders:
    divide_pan(0, 0, 2**n, 2**n, order)
    new_arr = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            if arr[i][j] == 0:
                continue
            ice_adj = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if not (0 <= nx < 2**n and 0 <= ny < 2**n):
                    continue
                if arr[nx][ny] == 0:
                    continue

                ice_adj += 1
            
            if ice_adj < 3:
                new_arr[i][j] = arr[i][j] - 1
            else:
                new_arr[i][j] = arr[i][j]
    
    arr = new_arr[:]

volume = 0
ans = 0
for i in range(2**n):
    for j in range(2**n):
        if not visited[i][j] and arr[i][j] != 0:
            ans = max(ans, bfs(arr, i, j))
        
        if arr[i][j] != 0:
            volume += arr[i][j]

print(volume)
print(ans)