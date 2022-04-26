from copy import deepcopy
from itertools import product
from pprint import pprint
import sys
input = sys.stdin.readline


m, s = map(int,input().split())
fish_bowl = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(m):
    fx, fy, d = map(int, input().split())
    fish_bowl[fx-1][fy-1].append(d-1)

sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1

shark_route = product(range(0, 4), range(0, 4), range(0, 4))
    
def count_fish(arr):

    length = 0
    for i in range(4):
        for j in range(4):
            length += len(arr[i][j])
    
    return length

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

number = 0
answer = 0
while True:
    print(f"--------------{number+1}단계!--------------")
    if number >= s:
        answer = count_fish(fish_bowl)
        break

    # TODO 1. 물고기 복제
    copy_bowl = deepcopy(fish_bowl)

    # TODO 2. 물고기 이동
    after_move_fish = [[[] for _ in range(4)] for _ in range(4)]
    # pprint(fish_bowl)
    for i in range(4):
        for j in range(4):
            while fish_bowl[i][j]:
                f_d = fish_bowl[i][j].pop()
                for k in range(8):
                    n_d = f_d - k if f_d - k >= 0 else 8 + (f_d - k)
                    # print(n_d)
                    nx, ny = i + dx[n_d], j + dy[n_d]

                    if not (0 <= nx < 4 and 0 <= ny < 4): continue
                    if nx == sx and ny == sy: continue
                    if smell[nx][ny]: continue

                    after_move_fish[nx][ny].append(n_d)
                    break
                else:
                    after_move_fish[i][j].append(f_d)
    
    # TODO 3. 상어 이동 파악
    print("-----시작------")
    direct = []
    for i in range(64):
        init_x, init_y = sx, sy
        route = set()
        print(shark_route[i])
        for d in shark_route[i]:
            nx, ny = init_x + sdx[d], init_y + sdy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                route.add((nx, ny))
            init_x, init_y = nx, ny
        num = 0
        for x, y in route:
            num += len(after_move_fish[x][y])
        print(list(sr)+[num])
        direct.append(list(sr)+[num])
    route.clear()
    print(direct)
    direct.sort(key=lambda x: [-x[3], x[0], x[1], x[2]])
    shark_rou = direct[0]
    print("------끝-------")
    pprint(after_move_fish)
    
    # TODO 4. 이동하면서 물고기 있는 자리 냄새 처리
    for i in range(3):
        nx, ny = sx + sdx[shark_rou[i]], sy + sdy[shark_rou[i]]
        fish_number = len(after_move_fish[nx][ny])
        if fish_number > 0:
            smell[nx][ny] = number
            after_move_fish[nx][ny].clear()
        sx, sy = nx, ny

    # TODO 5. 전전 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if abs(number - smell[i][j]) >= 2:
                smell[i][j] = 0
        
    
    # TODO 6. 물고기 복제 완료
    for i in range(4):
        for j in range(4):
            while copy_bowl[i][j]:
                n_fish = copy_bowl[i][j].pop()
                after_move_fish[i][j].append(n_fish)
    
    fish_bowl = deepcopy(after_move_fish)
    number += 1
    
print(answer)