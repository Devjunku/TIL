from pprint import pprint
from math import ceil
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sx, sy = n//2, n//2
print(sx, sy)
# 이동 크기
move_size = 1
move_flag = 0
direct = [[0, -1], [1, 0], [0, 1], [-1, 0]]
ans = 0

selt_direct = [
    [
        [-1, 0, 1],
        [1, 0, 1],
        [-1, -1, 7],
        [1, -1, 7],
        [-2, -1, 2],
        [2, -1, 2],
        [-1, -2, 10],
        [1, -2, 10],
        [0, -3, 5]
    ],
    [
        [0, 1, 1],
        [0, -1, 1],
        [1, -1, 7],
        [1, 1, 7],
        [1, -2, 2],
        [1, 2, 2],
        [2, -1, 10],
        [2, 1, 10],
        [3, 0, 5]
    ],
    [
        [-1, 0, 1],
        [1, 0, 1],
        [-1, 1, 7],
        [1, 1, 7],
        [-2, 1, 2],
        [2, 1, 2],
        [-1, 2, 10],
        [1, 2, 10],
        [0, 3, 5]
    ],
    [
        [0, 1, 1],
        [0, -1, 1],
        [-1, -1, 7],
        [-1, 1, 7],
        [-1, -2, 2],
        [-1, 2, 2],
        [-2, -1, 10],
        [-2, 1, 10],
        [-3, 0, 5]
    ]
]

def salt_moving(sx, sy, nx, ny, d):
    global ans

    for nd in selt_direct[d]:
        x, y = sx + nd[0], sy + nd[1]
        if not (0 <= x < n and 0 <= y <n):
            ans += int(arr[nx][ny] * (nd[2]/100))
        else:
            arr[x][y] += int(arr[nx][ny] * (nd[2]/100))
    
    if d == 0:
        if (0 <= sx < n and 0 <= sy-2 < n):
            arr[sx][sy-2] += int(arr[nx][ny]*((100 - 45)/100))
        else:
            ans += int(arr[nx][ny]*((100 - 45)/100))
    elif d == 1:
        if (0 <= sx+2 < n and 0 <= sy < n):
            arr[sx+2][sy] += int(arr[nx][ny]*((100 - 45)/100))
        else:
            ans += int(arr[nx][ny]*((100 - 45)/100))
    elif d == 2:
        if (0 <= sx < n and 0 <= sy+2 < n):
            arr[sx][sy+2] += int(arr[nx][ny]*((100 - 45)/100))
        else:
            ans += int(arr[nx][ny]*((100 - 45)/100))
    elif d == 3:
        if (0 <= sx-2 < n and 0 <= sy-2 < n):
            arr[sx-2][sy] += int(arr[nx][ny]*((100 - 45)/100))
        else:
            ans += int(arr[nx][ny]*((100 - 45)/100))

    arr[nx][ny] = 0

while True:
    if move_size != n-1:
        # flagg만 바뀌는 상태로 2번 이동해야함.
        d = direct[move_flag%4]
        for _ in range(move_size):
            nx, ny = sx + d[0], sy + d[1]
            salt_moving(sx, sy, nx, ny, move_flag%4)
            sx, sy = nx, ny
        move_flag += 1
        
        pprint(arr)
        d = direct[move_flag%4]
        for _ in range(move_size):
            nx, ny = sx + d[0], sy + d[1]
            salt_moving(sx, sy, nx, ny, move_flag%4)
            sx, sy = nx, ny
        move_flag += 1
        move_size += 1
        pprint(arr)

    else:
        # flagg만 바뀌는 상태로 2번 이동해야함.
        d = direct[move_flag%4]
        for _ in range(move_size):
            nx, ny = sx + d[0], sy + d[1]
            salt_moving(sx, sy, nx, ny, move_flag%4)
            sx, sy = nx, ny
        
        pprint(arr)
        
        move_flag += 1
        d = direct[move_flag%4]
        for _ in range(move_size):
            nx, ny = sx + d[0], sy + d[1]
            salt_moving(sx, sy, nx, ny, move_flag%4)
            sx, sy = nx, ny

        pprint(arr)
        
        move_flag += 1
        d = direct[move_flag%4]
        for _ in range(move_size):
            nx, ny = sx + d[0], sy + d[1]
            salt_moving(sx, sy, nx, ny, move_flag%4)
            sx, sy = nx, ny
        
        pprint(arr)
        break

print(ans)