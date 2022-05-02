from copy import deepcopy
from itertools import product
from pprint import pprint
import sys
input = sys.stdin.readline

bowl = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

# 방향은 8 이하의 자연수로 표현하고, 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

m, s = map(int, input().split())

shark_move = list(product(range(0, 4), range(0, 4), range(0, 4)))
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]
for _ in range(m):
    fx, fy, d = map(int, input().split())
    bowl[fx-1][fy-1].append(d-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for _ in range(s):

    # TODO 모든 칸 복제
    copy_bowl = deepcopy(bowl)

    # pprint(bowl)
    # TODO 물고기 이동
    new_bowl = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            x, y = i, j
            while bowl[i][j]:
                fd = bowl[i][j].pop()
                for k in range(8):
                    nd = (fd + 7) % 8
                    nx, ny = x + dx[fd], y + dy[fd]
                    if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                        fd = nd
                        continue
                    if smell[nx][ny] > 0:
                        fd = nd
                        continue

                    new_bowl[nx][ny].append(fd)
                    break
                else:
                    new_bowl[i][j].append(fd)
    
    bowl = deepcopy(new_bowl)

    # 상어 이동 전에 냄새 1 삭제
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1


    # TODO 상어 이동 루트 파악
    shark_routes = []
    for s_m in shark_move:
        route_value = set()
        flag = 0
        x, y = sx, sy
        for d in s_m:
            nx, ny = x + sdx[d], y + sdy[d]
            if not (0 <= nx < 4 and 0 <= ny < 4):
                flag = 1
                break
            route_value.add((nx, ny))
            x, y = nx, ny
        
        if flag: continue
        num = 0
        for x, y in route_value:
            num += len(bowl[x][y])
        shark_routes.append(list(s_m) + [num])
    shark_routes.sort(key=lambda x: [-x[3], x[0], x[1], x[2]])
    route = shark_routes[0]
    # TODO 상어 이동
    for d in range(0, 3):
        nx, ny = sx + sdx[route[d]], sy + sdy[route[d]]
        if bowl[nx][ny]:
            bowl[nx][ny].clear()
            smell[nx][ny] = 2
        sx, sy = nx, ny
    
    # TODO 상어 복제
    for i in range(4):
        for j in range(4):
            while copy_bowl[i][j]:
                bowl[i][j].append(copy_bowl[i][j].pop())
    # pprint(bowl)
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(bowl[i][j])

print(answer)







