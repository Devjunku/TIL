from collections import deque
import sys
input = sys.stdin.readline

N, q = map(int, input().split())

arr = []

for _ in range(2**N):
    arr.append(list(map(int, input().split())))

shark_lv = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def ice_sum(arr):
    res = 0
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] > 0: res += arr[i][j]
    
    return res


def ice_block(arr):

    q = deque([])
    num = len(arr)

    visited = [[0 for _ in range(num)] for _ in range(num)]
    res = 0
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] > 0 and visited[i][j] == 0:
                visited[i][j] = 1
                q.append((i, j))
                ice_number = 1

                while q:
                    x, y = q.popleft()
                     
                    for k in range(4):

                        nx, ny = x + dx[k], y + dy[k]

                        if not (0 <= nx < 2**N and 0 <= ny < 2**N): continue
                        if visited[nx][ny] != 0: continue
                        if arr[nx][ny] <= 0: continue

                        visited[nx][ny] = 1
                        ice_number += 1
                        q.append((nx, ny))
                res = max(res, ice_number)
    
    return res


def rotate_90(arr):
    reverse_list = zip(*arr[::-1])
    return [list(elem) for elem in reverse_list]


def recursive(n, level, sx, sy, ex, ey):
    global arr

    if n == level:
        res = []
        for i in range(sx, ex):
            ll = []
            for j in range(sy, ey):
                ll.append(arr[i][j])
            res.append(ll)

        res = rotate_90(res)
        
        for i in range(2**level):
            for j in range(2**level):
                arr[sx+i][sy+j]=res[i][j]
        return
    
    recursive(n-1, level, sx, sy, (sx+ex)//2, (sy+ey)//2)
    recursive(n-1, level, sx, (sy+ey)//2, (ex+sx)//2, ey)
    recursive(n-1, level, (sx+ex)//2, sy, ex, (sy+ey)//2)
    recursive(n-1, level, (sx+ex)//2, (sy+ey)//2, ex, ey)
    


for l in shark_lv:
    recursive(N, l, 0, 0, 2**N, 2**N)
    copy_arr = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j] == 0: continue
            adj_ice_num = 0

            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if not (0 <= nx < 2**N and 0 <= ny < 2**N): continue
                if arr[nx][ny] <= 0: continue
                adj_ice_num += 1
            
            if adj_ice_num < 3:
                copy_arr[i][j] = arr[i][j] - 1 if arr[i][j] > 0 else  0
            else:
                copy_arr[i][j] = arr[i][j]
    arr = copy_arr

print(ice_sum(arr))
print(ice_block(arr))