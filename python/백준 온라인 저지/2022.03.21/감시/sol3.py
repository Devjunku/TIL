from pprint import pprint
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

corridor = []
cctv_loc = []
cctv_num = 0
zero = 0
for i in range(n):
    corridor.append(list(map(int, input().split())))
    for j in range(m):
        if corridor[i][j] in [1, 2, 3, 4, 5]:
            cctv_loc.append((i, j))
            cctv_num += 1
        elif corridor[i][j] == 0:
            zero += 1
cctv_loc.append((-1, -1))
dx = [0, -1, 0, 1] # 동 북 서 남
dy = [1, 0, -1, 0]


cctv_direct = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

def dfs(arr, x, y, direct, num):
    global zero
    pprint(arr)
    if x == -1 and y == -1:
        zero_cnt = 0
        for i in range(n):
            zero_cnt += arr[i].count(0)
        zero = min(zero, zero_cnt)
        return
    
    for cctv_d in cctv_direct[direct]:
        for dire in cctv_d:
            nx, ny = x + dx[dire], y + dy[dire]
            while True:

                if not (0 <= nx < n and 0 <= ny < m):
                    break
                
                if arr[nx][ny] in [1, 2, 3, 4, 5]:
                    nx += dx[dire]
                    ny += dy[dire]
                    continue
        
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 7

                nx += dx[dire]
                ny += dy[dire]
            
        dfs(arr, cctv_loc[num][0], cctv_loc[num][1], corridor[cctv_loc[num][0]][cctv_loc[num][1]],num + 1)

        for dire in cctv_d:
            nx, ny = x + dx[dire], y + dy[dire]
            while True:

                if not (0 <= nx < n and 0 <= ny < m):
                    break
                
                if arr[nx][ny] in [1, 2, 3, 4, 5]:
                    nx += dx[dire]
                    ny += dy[dire]
                    continue
        
                if arr[nx][ny] == 7:
                    arr[nx][ny] = 0

                nx += dx[dire]
                ny += dy[dire]

dfs(corridor, cctv_loc[0][0], cctv_loc[0][1], corridor[cctv_loc[0][0]][cctv_loc[0][1]], 1)
print(zero)