from itertools import product
from heapq import heappush
from copy import deepcopy
import sys
from pprint import pprint
input = sys.stdin.readline

# 냄새 표시 -2
# 상어 표시 -1
# 물고리 표시 1
# 빈칸 표시 0

fish_num, s = map(int, input().split())
bowl = [[[] for _ in range(4)] for _ in range(4)]
# pprint(bowl)
fdx = [0, -1, -1, -1, 0, 1, 1, 1]
fdy = [-1, -1, 0, 1, 1, 1, 0, -1]

sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

for _ in range(fish_num):
    fx, fy, d = map(int, input().split())
    bowl[fx-1][fy-1].append([1, d-1, 0])

sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1


shark_direct = product(range(4), range(4), range(4))

# pprint(bowl)
answer = 0
def cal_fish_number(sx, sy, number, bowl):
    global answer
    print(sx, sy)

    if number >= s:
        return

    # TODO 물고기 복제!
    copy_bowl = deepcopy(bowl)

    # TODO bowl 물고기 이동!
    # 1. 한칸만 이동!
    # 2. 상어가 있는 칸, 물고기 냄새가 있는 칸, 격자 범위를 벗어나는 칸은 못간다.
    # 3. 이동할 수 없으면 45도 회전
    # 4. 이동할 수 있는 칸이 없으면 이동하지 않는다.

    new_bowl = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while bowl[i][j]:
                fish = bowl[i][j].pop()
                # 물고기가 아닌 경우 그냥 새로운 어항에 넣어줌
                if fish[0] != 1:
                    new_bowl[i][j].append(fish)
                    continue
                
                fd = fish[1] # 물고기가 바라보는 방향
                for k in range(8):
                    # 반시계 방향
                    if (fd-k) >= 0:
                        nd = (fd-k) % 8
                    else:
                        nd = 8 + (fd-k)
                    nx, ny = i + fdx[nd], j + fdy[nd]

                    # 격자 밖은 안됨
                    if not (0 <= nx < 4 and 0 <= ny < 4): continue
                    # 상어가 있으면 안됨
                    if nx == sx and ny == sy: continue
                    # 새로운 어항 또는 기존의 어항에서 냄새가 있는 칸은 안됨
                    toggle = False
                    for data in bowl[nx][ny]:
                        if data[0] == -2:
                            toggle = True
                            break
                    
                    for data in new_bowl[nx][ny]:
                        if data[0] == -2:
                            toggle = True
                            break

                    if toggle: continue

                    # 이제 방향 수정 후 이동 가능
                    new_bowl[nx][ny].append([fish[0], nd, number])
                    break
    
    # TODO 냄새 지우기!
    # 두 번 전에 연습에서 남은 냄새 지우기
    not_smell_new_bowl = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while new_bowl[i][j]:
                fish = new_bowl[i][j].pop()
                if fish[0] == -2 and (number - fish[2]) >= 2:
                    continue
                not_smell_new_bowl[i][j].append(fish)

    # TODO 상어 이동 판단!!
    # 연속 3칸 이동
    # 인접한 상하좌우만 이동 가능
    # 격자는 지켜져야 함
    # 먼저 연속해서 이동할 수 있는 칸을 계산
    shark_can_go = []
    # print(f"number: {number}")




    for sd in shark_direct:
        print(f"number: {number}")
        x, y = sx, sy
        toggle = False
        eat_fish_num = 0
        alreay_go = []
        alreay_go.append((x, y))
        # print(sd)
        for nsd in sd:
            nx, ny = x + sdx[nsd], y + sdy[nsd]
            # 격자 밖 또는 전에 갔던 곳은 break
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx, ny) in alreay_go:
                print(f"number: {number}")
                toggle = True
                break

            eat_fish_num += sum([1 if fish[0] == 1 else 0 for fish in not_smell_new_bowl[nx][ny]])
            x, y = nx, ny
            alreay_go.append((nx, ny))

        print(toggle)
        if not toggle:
            heappush(shark_can_go, tuple([-eat_fish_num] + list(sd)))
        
    print(shark_can_go)
    # shark_can_go.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
    can_go = list(shark_can_go[0])
    
    # TODO 냄새 생성 및 상어 이동 이때 물고기 제거 해줘야 함.
    for i in range(1, 4):
        nx, ny = sx + sdx[can_go[i]] , sy + sdy[can_go[i]]
        smell = []
        data = not_smell_new_bowl[nx][ny][:]
        for fish in data:
            if fish[0] == 1:
                fish[0] = -2
                fish[2] = number
                smell.append(fish)
                break
        not_smell_new_bowl[nx][ny].clear()
        not_smell_new_bowl[nx][ny].extend(smell)
        sx, sy = nx, ny


    # TODO 복제한거 넣어줘야함.
    for i in range(4):
        for j in range(4):
            while copy_bowl[i][j]:
                fish = copy_bowl[i][j].pop()
                if fish[0] == 1:
                    not_smell_new_bowl[i][j].append(fish)


    # 물고기 개수 세기
    fish_lv_num = 0
    for i in range(4):
        for j in range(4):
            if not_smell_new_bowl[i][j]:
                for fish in not_smell_new_bowl[i][j]:
                    if fish[0] == 1:
                        fish_lv_num += 1
    
    # 정답 업데이트 시키고
    answer = max(answer, fish_lv_num)
    # pprint(not_smell_new_bowl)

    cal_fish_number(sx, sy, number+1, deepcopy(not_smell_new_bowl))

cal_fish_number(sx, sy, 0, bowl)
print(answer)