from copy import deepcopy
import sys
from itertools import product
input = sys.stdin.readline

m, s = map(int, input().split())
bowl = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]
shark_move = list(product(range(4), range(4), range(4)))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

s_dx = [-1, 0, 1, 0]
s_dy = [0, -1, 0, 1]

for _ in range(m):
    x, y, d = map(int, input().split())
    bowl[x-1][y-1].append(d-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for rounding in range(1, s+1):
    # TODO 물고기 복제
    bowl_copy = deepcopy(bowl)
    bowl_move = [[[] for _ in range(4)] for _ in range(4)]

    # TODO 물고기 이동
    for i in range(4):
        for j in range(4):
            while bowl[i][j]:
                fd = bowl[i][j].pop()
                for _ in range(8):
                    nx, ny = i + dx[fd], j + dy[fd]

                    if not (0 <= nx < 4 and 0 <= ny < 4):
                        fd = (fd + 7) % 8
                        continue

                    if smell[nx][ny] > 0 or (nx == sx and ny == sy):
                        fd = (fd + 7) % 8
                        continue

                    bowl_move[nx][ny].append(fd)
                    break
                else:
                    bowl_move[i][j].append(fd)
    
    # TODO 상어 이동 경로 파악
    shark_routes = []
    for s_m in shark_move:
        route_value = set()
        flag = 0
        x, y = sx, sy
        for d in s_m:
            nx, ny = x + s_dx[d], y + s_dy[d]
            if not (0 <= nx < 4 and 0 <= ny < 4):
                flag = 1
                break
            route_value.add((nx, ny))
            x, y = nx, ny
        
        if flag: continue

        num = 0
        for x, y in route_value:
            num += len(bowl_move[x][y])
        shark_routes.append(list(s_m) + [num])
        
    shark_routes.sort(key=lambda x: [-x[3], x[0], x[1], x[2]])
    route = shark_routes[0]

    # TODO 상어 이동
    for i in range(3):
        nx, ny = sx + s_dx[route[i]], sy + s_dy[route[i]]
        if bowl_move[nx][ny]:
            smell[nx][ny] = rounding
            bowl_move[nx][ny].clear()
        sx, sy = nx, ny
    

    # TODO 냄새 없애기
    for i in range(4):
        for j in range(4):
            if abs(smell[i][j] - rounding) == 2:
                smell[i][j] = 0
    
    # TODO 물고기 추가
    for i in range(4):
        for j in range(4):
            while bowl_copy[i][j]:
                fish = bowl_copy[i][j].pop()
                bowl_move[i][j].append(fish)
    bowl = deepcopy(bowl_move)

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(bowl[i][j])

print(answer)