from pandas import DataFrame
import sys
input = sys.stdin.readline

fishbowl = [[0 for _ in range(4)] for _ in range(4)]
directbowl = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    l = list(map(int, input().split()))
    for j in range(0, 8, 2):
        fishbowl[i][j//2] = l[j]
        directbowl[i][j//2] = l[j+1]-1

cnt = fishbowl[0][0]
fishbowl[0][0] = 17
# 상어는 17로 표현하고
# 아무도 없는 공간에 대한 방향은 -1로 하자
# 근데 1부터 16까지 어떻게 옮길건데?
# 이동하면서 계속 위치가 바뀔텐데..
# 상어가 움직일때만 dfs로 넘기고
# 물고기가 옮겨지는 과정은 한 번에 진행해야 할거 같은데
# 그냥 다 돌고 확인하고 옮기는게 좋을거 같다

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def isCanGoToRoom(x, y, fish_bowl, direct_bowl):
    direct = direct_bowl[x][y]
    for i in range(8):
        nx, ny = x + dx[(direct+i)%8], y + dy[(direct+i)%8]
        
        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if fish_bowl[nx][ny] == 17:
            continue

        return (True, (direct+i)%8)

    return (False, None)



def eat_fish(fish_bowl, direct_bowl, weight):
    global cnt
    print(DataFrame(fish_bowl))
    print(DataFrame(direct_bowl))
    print("-------------")
    cnt = max(cnt, weight)
    # 물고기 이동!
    for fish in range(1, 17):
        isFish = False
        x, y = -1, -1
        for i in range(4):
            for j in range(4):
                if fish_bowl[i][j] == fish:
                    isFish = True
                    x, y = i, j
                    break
            if isFish:
                break
        if isFish:
            result = isCanGoToRoom(x, y, fish_bowl, direct_bowl)
            if result[0]:
                direct_bowl[x][y] = result[1]
                # print(result)
                fish_bowl[x][y], fish_bowl[x+dx[result[1]]][y+dy[result[1]]] = fish_bowl[x+dx[result[1]]][y+dy[result[1]]], fish_bowl[x][y]
                direct_bowl[x][y], direct_bowl[x+dx[result[1]]][y+dy[result[1]]] = direct_bowl[x+dx[result[1]]][y+dy[result[1]]], direct_bowl[x][y]

    # pprint(direct_bowl)
    # 상어 찾기
    for i in range(4):
        for j in range(4):
            if fish_bowl[i][j] == 17:
                shark_x, shark_y = i, j
                shark_direct = direct_bowl[i][j]
                break
    
    # 상어가 갈 수 있는 곳 보기
    canGoRoom = []
    for i in range(1, 5):
        if not (0 <= shark_x+dx[shark_direct]*i < 4 and 0 <= shark_y+dy[shark_direct]*i < 4):
            continue
        if fish_bowl[shark_x+dx[shark_direct]*i][shark_y+dy[shark_direct]*i] == 0:
            continue
        canGoRoom.append((shark_x+dx[shark_direct]*i, shark_y+dy[shark_direct]*i))
    
    for goRoom in canGoRoom:
        origin_fish = fish_bowl[goRoom[0]][goRoom[1]]
        if origin_fish == 0:
            continue
        fish_bowl[goRoom[0]][goRoom[1]] = 17
        fish_bowl[shark_x][shark_y] = 0
        direct_bowl[shark_x][shark_y] = -1
        eat_fish(fish_bowl, direct_bowl, weight+origin_fish)
        fish_bowl[shark_x][shark_y] = 17
        fish_bowl[goRoom[0]][goRoom[1]] = origin_fish
        direct_bowl[shark_x][shark_y] = shark_direct

eat_fish(fishbowl, directbowl, cnt)
print(cnt)