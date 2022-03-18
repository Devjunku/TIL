from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())

maze = [list(input().strip()) for _ in range(n)]

can_flee = False

red = []
blue = []
for i in range(n):
    for j in range(m):
        if maze[i][j] == "R":
            red = [i, j]
        elif maze[i][j] == "B":
            blue = [i, j]
print(red, blue)
dic = {
    1: (0, 1), # 오른쪽 → 더 오른쪽에 있는 구슬이 먼저 움직임
    2: (0, -1), # 왼쪽 → 더 왼쪽에 있는 구슬이 먼저 움직임
    3: (1, 0), # 위 → 더 위쪽에 있는 구슬이 먼저 움직임
    4: (-1, 0) # 아래 → 더 아래쪽에 있는 구슬이 먼저 움직임
}

# 두번만 반복해서 움직이면 굳이 구분안해도 됨
def isFlee(idx_arr, _maze, red_loc, blue_loc):
    global can_flee

    red_flee = False
    blue_flee = False

    # pprint(_maze)
    print(idx_arr)
    for idx in range(10):

        # print(f"새로운 index 시작: {idx}, {dic[idx_arr[idx]]}")
        for _ in range(2):
            # Blue
            x, y = blue_loc[0], blue_loc[1]
            while True:
                nx, ny = x + dic[idx_arr[idx]][0], y + dic[idx_arr[idx]][1]
                if not (0 <= nx < n and 0 <= ny < m):
                    break

                if _maze[nx][ny] == "#" or _maze[nx][ny] == "R":
                    _maze[blue_loc[0]][blue_loc[1]] = "."
                    blue_loc[0], blue_loc[1] = x, y
                    _maze[blue_loc[0]][blue_loc[1]] = "B"
                    break

                if _maze[nx][ny] == "O":
                    _maze[blue_loc[0]][blue_loc[1]] = "."
                    blue_flee = True
                    break

                x, y = nx, ny
            # Red
            x, y = red_loc[0], red_loc[1]
            while True:
                nx, ny = x + dic[idx_arr[idx]][0], y + dic[idx_arr[idx]][1]

                if not (0 <= nx < n and 0 <= ny < m):
                    break

                if _maze[nx][ny] == "#" or _maze[nx][ny] == "B":
                    _maze[red_loc[0]][red_loc[1]] = "."
                    red_loc[0], red_loc[1] = x, y
                    _maze[red_loc[0]][red_loc[1]] = "R"
                    break

                print(f"red: {nx}, {ny}, {dic[idx_arr[idx]]}")
                print(f"blue: {blue_loc[0]}, {blue_loc[1]}, {dic[idx_arr[idx]]}")
                if _maze[nx][ny] == "O":
                    # print(nx, ny)
                    _maze[red_loc[0]][red_loc[1]] = "."
                    red_flee = True
                    break

                x, y = nx, ny
        if blue_flee:
            return
        elif red_flee:
            # pprint(_maze)
            # print(idx_arr)
            # print(idx)
            can_flee = True
            return
        

def Hpermutation(num, idx_arr):

    if can_flee:
        return

    if len(idx_arr) >= 2:
        if idx_arr[-1] == idx_arr[-2]:
            return

    if num == 10:
        isFlee(idx_arr, deepcopy(maze), red, blue)
        return

    for i in range(1, 5):
        if can_flee:
            continue
        idx_arr.append(i)
        Hpermutation(num+1, idx_arr)
        idx_arr.pop()

Hpermutation(0, [])

if can_flee:
    print(1)
else:
    print(0)