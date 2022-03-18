from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

arr = []
red_x, red_y = 0, 0
blue_x, blue_y = 0, 0

for i in range(n):
    arr.append(list(input().strip()))
    for j in range(m):
        if arr[i][j] == "R":
            red_x, red_y = i, j
            arr[i][j] = "."
        elif arr[i][j] == "B":
            blue_x, blue_y = i, j
            arr[i][j] = "."

    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move(x, y, dx, dy):
    nx, ny = x, y
    moving = 0

    while True:
        # R, B에 상관없이 일단은 이동한다
        # 대신에 움직인 거리를 계산한다
        if arr[nx + dx][ny + dy] != "#" and arr[nx + dx][ny + dy] != "O":
            nx += dx
            ny += dy
            moving += 1
        else:
            break
    
    return nx, ny, moving

def bfs():
    q = deque()
    q.append((red_x, red_y, blue_x, blue_y, 0))

    while q:
        x, y, a, b, count = q.popleft()
        
        if count > 10:
            continue

        for k in range(4):
            nx, ny, Rmove = move(x, y, dx[k], dy[k])
            na, nb, Bmove = move(a, b, dx[k], dy[k])

            # 움직인 후에 blue를 먼저 살펴본다. 굿~!
            if arr[na + dx[k]][nb + dy[k]] == "O":
                continue
            
            if arr[nx + dx[k]][ny + dy[k]] == "O" and count < 10:
                return 1
            
            if nx == na and ny == nb:
                if Rmove > Bmove:
                    nx -= dx[k]
                    ny -= dy[k]
                else:
                    na -= dx[k]
                    nb -= dy[k]
            
            # 움직였는데, 의미가 없는 경우는 q에 추가하지 않고 넘어감
            if x == nx and y == ny and na == a and nb == b:
                continue
            
            # 움직였는데 의미가 있는 경우에는 q에 추가하고 넘어감
            q.append((nx, ny, na, nb, count + 1))
    
    return 0

result = bfs()
print(result)



