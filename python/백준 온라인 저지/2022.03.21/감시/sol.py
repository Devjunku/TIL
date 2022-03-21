import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 1일때는 할 수 있는 방향이 4곳, 4로 나눈 너머지를 사용하면 됨 1개
# 2일때는 4로 나눈 나머지인데 +1 나머지에도 +1해야함 2개
# 3일때는 4로 나눈 나머지인데 +2 나머지에 +2 2개
# 4일 때는 한번에 3개 이기 때문에 할 때 마다 +3 에서 3개다 끌어와야함
# 5일 때는 걍 1번에 다 보면 됨

cannot_cctv = 0
cctv_num = 0
cctv_list = []
for i in range(n):
    for j in range(m):
        if room[i][j] in [1, 2, 3, 4, 5]:
            cctv_list.append((i, j))
            cctv_num += 1
        elif room[i][j] == 0:
            cannot_cctv += 1

cctv_list.append((-1, -1))

def dfs(x, y, direct, c_num):
    global cannot_cctv, room

    if x == -1 and y == -1:
        zero_num = 0
        for i in range(n):
            for j in range(m):
                if room[i][j] == 0:
                    zero_num += 1
        cannot_cctv = min(cannot_cctv, zero_num)
        return
        
    room2 = deepcopy(room)
    if direct == 1:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                
                if room[nx][ny] == 6:
                    break

                if room[nx][ny] in [1, 2, 3, 4, 5]:
                    nx, ny = nx + dx[i], ny + dy[i]
                    continue
                room[nx][ny] = "#"
                nx, ny = nx + dx[i], ny + dy[i]
            dfs(cctv_list[c_num][0], cctv_list[c_num][1], room[cctv_list[c_num][0]][cctv_list[c_num][1]], c_num+1)
            room = deepcopy(room2)  
    elif direct == 2:
        for j in range(2):
            for i in range(j, 4, 2):
                nx, ny = x + dx[i], y + dy[i]
                while True:
                    if not (0 <= nx < n and 0 <= ny < m):
                        break
                    
                    if room[nx][ny] == 6:
                        break

                    if room[nx][ny] in [1, 2, 3, 4, 5]:
                        nx, ny = nx + dx[i], ny + dy[i]
                        continue
                    room[nx][ny] = "#"
                    nx, ny = nx + dx[i], ny + dy[i]
            dfs(cctv_list[c_num][0], cctv_list[c_num][1], room[cctv_list[c_num][0]][cctv_list[c_num][1]], c_num+1)
            room = deepcopy(room2)  
    elif direct == 3:
        for i in range(4):
            for j in range(i, i+2):
                nx, ny = x + dx[j%4], y + dy[j%4]
                while True:
                    if not (0 <= nx < n and 0 <= ny < m):
                        break
                    
                    if room[nx][ny] == 6:
                        break

                    if room[nx][ny] in [1, 2, 3, 4, 5]:
                        nx, ny = nx + dx[i], ny + dy[i]
                        continue
                    room[nx][ny] = "#"
                    nx, ny = nx + dx[j%4], ny + dy[j%4]
            dfs(cctv_list[c_num][0], cctv_list[c_num][1], room[cctv_list[c_num][0]][cctv_list[c_num][1]], c_num+1)
            room = deepcopy(room2)
    elif direct == 4:
        for i in range(4):
            for j in range(i, i+3):
                nx, ny = x + dx[j%4], y + dy[j%4]
                while True:
                    if not (0 <= nx < n and 0 <= ny < m):
                        break
                    
                    if room[nx][ny] == 6:
                        break

                    if room[nx][ny] in [1, 2, 3, 4, 5]:
                        nx, ny = nx + dx[i], ny + dy[i]
                        continue
                    room[nx][ny] = "#"
                    nx, ny = nx + dx[j%4], ny + dy[j%4]
            dfs(cctv_list[c_num][0], cctv_list[c_num][1], room[cctv_list[c_num][0]][cctv_list[c_num][1]], c_num+1)
            room = deepcopy(room2)
    elif direct == 5:
        for i in range(4):
            nx, ny = x + dx[i%4], y + dy[i%4]
            while True:
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                
                if room[nx][ny] == 6:
                    break

                if room[nx][ny] in [1, 2, 3, 4, 5]:
                    nx, ny = nx + dx[i], ny + dy[i]
                    continue
                room[nx][ny] = "#"
                nx, ny = nx + dx[i%4], ny + dy[i%4]
        dfs(cctv_list[c_num][0], cctv_list[c_num][1], room[cctv_list[c_num][0]][cctv_list[c_num][1]], c_num+1)
        room = deepcopy(room2)

if cctv_num == 0:
    print(cannot_cctv)
else:
    dfs(cctv_list[0][0], cctv_list[0][1], room[cctv_list[0][0]][cctv_list[0][1]], 1)
    print(cannot_cctv)