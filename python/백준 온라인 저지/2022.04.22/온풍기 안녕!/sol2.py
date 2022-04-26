from collections import deque
from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline

"""
1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
2. 온도가 조절됨
3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4. 초콜릿을 하나 먹는다.
5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
"""
cho_cnt = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

r, c, k  = map(int, input().split())
confirm_point = []
warm_machine = []
arr = [[0 for _  in range(c)] for _ in range(r)]

bound_point = []
for i in range(r):
    for j in range(c):
        if i == 0:
            bound_point.append((i, j))
        elif j == c-1:
            bound_point.append((i, j))
        elif j == 0:
            bound_point.append((i, j))
        elif i == r-1:
            bound_point.append((i, j))

# 펼쳐질 때
wind_d = [
    [[[-1, 0], [0, 1]], [[0, 1]], [[1, 0], [0, 1]]],
    [[[-1, 0], [0, -1]], [[0, -1]], [[1, 0], [0, -1]]],
    [[[0, -1], [-1, 0]], [[-1, 0]], [[0, 1], [-1, 0]]],
    [[[0, -1], [1, 0]], [[1, 0]], [[0, 1], [1, 0]]]
]

for i in range(r):
    data = list(map(int, input().split()))
    for j in range(c):
        if data[j] == 5:
            confirm_point.append((i, j))
        elif data[j] in [1, 2, 3, 4]:
            warm_machine.append((i, j, data[j]-1))

w = int(input())
wall = set()
for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall.add((x, y, x-1, y))
        wall.add((x-1, y, x, y))
    else:
        wall.add((x, y, x, y+1))
        wall.append((x, y+1, x, y))

def confirm_k_up():
    cnt = 0
    for x, y in confirm_point:
        if arr[x][y] >= k:
            cnt += 1
    
    if cnt == len(confirm_point):
        return False
    
    return True

def spread_warm(d, value):
    visited = []
    while sub_point:
        x, y = sub_point.popleft()
        for routes in wind_d[d]:
            sx, sy = x, y
            for d_x, d_y in routes:
                nx, ny = sx + d_x, sy + d_y
                # 범위 벗어남
                if not (0 <= nx < r and 0 <= ny < c):
                    break
                
                # 벽 있음
                if (sx, sy, nx, ny) in wall or (nx, ny, sx, sy) in wall:
                    break
                sx, sy = nx, ny
            else:
                if (sx, sy) in visited:
                    break
                visited.append((sx, sy))
                # 위 모든 것에 break가 걸리지 않았으며
                # 값이 1보다 크면 다음 칸에 온도 전달 가능
                arr[sx][sy] += (value)
                if value > 1:
                    spread_point.append((sx, sy))

def deliver_adj_c():

    new_arr = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            
            plus = 0
            mius = 0
            for _d in range(4):
                nx, ny = i + dx[_d], j + dy[_d]
                # 범위 넘으면 안됨
                if not (0 <= nx < r and 0 <= ny < c):
                    continue

                # 벽있으면 안됨
                if (i, j, nx, ny) in wall or (nx, ny, i, j) in wall:
                    continue

                # 온도가 높은 칸에서 낮은 칸으로 온도가 이동하고 빠짐
                differ = abs(arr[i][j]-arr[nx][ny]) // 4
                if arr[i][j] > arr[nx][ny]:
                    mius += differ
                elif arr[nx][ny] > arr[i][j]:
                    plus += differ
            new_arr[i][j] += plus - mius   

    for i in range(r):
        for j in range(c):
            arr[i][j] += new_arr[i][j]

while confirm_k_up():

    if cho_cnt > 100:
        break

    # TODO 1, 2. 온풍기 나오고 온도 조절 됨
    # 온풍기 마다 바람이 나오므로 온풍기마다 방문 여부 체크하면서 해줘야함
    for x, y, d in warm_machine:
        sx, sy = x + dx[d], y + dy[d]
        v = 5
        if not (0 <= sx < r and 0 <= sy < c): continue
        arr[sx][sy] += v
        spread_point = deque([(sx, sy)])
        # 바람을 전달함
        while spread_point:
            sub_point = deepcopy(spread_point)
            spread_point.clear()
            if v > 1:
                spread_warm(d, v-1)
            v -= 1
    # 온도가 높은 곳에서 낮은 곳으로 전달됨
    deliver_adj_c()        

    # 가장 바깥쪽 온도만 1씩 낮아짐
    for x, y in bound_point:
        if arr[x][y] >= 1:
            arr[x][y] -= 1
    
    pprint(arr)
    cho_cnt += 1
    # break

if cho_cnt > 100:
    print(101)
else:
    print(cho_cnt)