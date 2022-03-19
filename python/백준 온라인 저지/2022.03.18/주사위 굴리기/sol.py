import sys
input = sys.stdin.readline

n, m, cx, cy, k = map(int, input().split())

mapping = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

orders = list(map(int, input().split()))
dice = [0 for _ in range(6)]

for order in orders:

    nx, ny = cx + dx[order], cy + dy[order]

    if not (0 <= nx < n and 0 <= ny < m):
        continue
    cx, cy = nx, ny
    
    # print(cx, cy, dice_x, dice_y)
    
    if order == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif order == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif order == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    if mapping[nx][ny] == 0:
        mapping[nx][ny] = dice[5]
    else:
        dice[5] = mapping[nx][ny]
        mapping[nx][ny] = 0
    
    print(dice[0])
    