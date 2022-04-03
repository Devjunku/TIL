from copy import deepcopy
from collections import deque
import sys

input = sys.stdin.readline

r, c, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

air_condition = []

for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            air_condition.append((i, j))
    if len(air_condition) == 2:
        break

def queue(start_x, start_y, direct):
    q = deque([0])
    d = 0
    while True:
        start_x += direct[d][0]
        start_y += direct[d][1]
        if not (0 <= start_x < r and 0 <= start_y < c):
            start_x -= direct[d][0]
            start_y -= direct[d][1]
            d += 1
            continue
        if arr[start_x][start_y] == -1:
            q.pop()
            break
        q.append(arr[start_x][start_y])
    return q


def air_loc(start_x, start_y, direct):
    q = []
    d = 0
    while True:
        start_x += direct[d][0]
        start_y += direct[d][1]
        if not (0 <= start_x < r and 0 <= start_y < c):
            start_x -= direct[d][0]
            start_y -= direct[d][1]
            d += 1
            continue
        if arr[start_x][start_y] == -1:
            break
        q.append((start_x, start_y))
    return q


fx, fy = air_condition[0][0], air_condition[0][1]
sx, sy = air_condition[1][0], air_condition[1][1]
# 공기청정기 방향 설정
first_direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]
second_direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

first_q = air_loc(fx, fy, first_direct)
second_q = air_loc(sx, sy, second_direct)

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dust = deque([]) #  먼지를 담을 Queue
while T > 0:

    # mapping 된 구역 초기화
    copy_arr = [[0 for _ in range(c)] for _ in range(r)]
    copy_arr[fx][fy] = -1
    copy_arr[sx][sy] = -1

    # 1 TODO: 머세먼지 확산 로직 작성
    # 기존 배열에서 먼지가 퍼지는 기준은 -> 먼지가 있는 구역인데, 먼지 찾아야 함

    # 먼지 담기
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                dust.append((i, j))
    
    # 먼지 이동
    while dust:
        x, y = dust.popleft()
        mius_dust = 0        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < r and 0 <= ny < c) or copy_arr[nx][ny] == -1:
                continue

            copy_arr[nx][ny] += int(arr[x][y]/5)
            mius_dust += int(arr[x][y]/5)
        
        copy_arr[x][y] += (arr[x][y] - mius_dust)
    
    arr = deepcopy(copy_arr)

    # 2 TODO: 공기청정기 작동
    d = 0
    start_x, start_y = fx, fy
    start_x += first_direct[d][0]
    start_y += first_direct[d][1]

    start_x, start_y = fx, fy
    q1 = queue(start_x, start_y, first_direct)

    start_x, start_y = sx , sy
    q2 = queue(start_x, start_y, second_direct)
        
    for i in range(len(first_q)):
        arr[first_q[i][0]][first_q[i][1]] = q1[i]

    for i in range(len(second_q)):
        arr[second_q[i][0]][second_q[i][1]] = q2[i]

    T -= 1

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != -1:
            answer += arr[i][j]

print(answer)