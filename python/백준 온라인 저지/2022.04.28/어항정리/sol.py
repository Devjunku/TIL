import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split()))]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

turn = 0

def check(arr):
    if max(arr) - min(arr) <= k:
        return False
    return True

def push():
    min_value = min(arr[-1])
    for i in range(n):
        if arr[-1][i] == min_value:
            arr[-1][i] += 1

def roll(arr):
    row, col = 1, 1
    new_n = n
    time = 0

    while True:
        new_Array = [[-1 for _ in range(new_n-col)] for _ in range(row+1)]

        for y in range(col, new_n):
            new_Array[-1][y-col] = arr[-1][y]

        for y in range(col):
            for x in range(len(arr)):
                new_Array[y][len(arr)-x-1] = arr[x][y]
                
        new_n -= col
        if time % 2:
            row += 1
            col += 1
        time += 1

        arr = [elem[:] for elem in new_Array]
        row_n = len(new_Array)
        if row_n * (col+1) > n:
            break
    
    return arr

def out_bound(x, y, row, col):
    if 0 <= x < row and 0 <= y < col:
        return False
    return True

def blow():
    row = len(new_arr)
    col = len(new_arr[0])
    temp = [[0 for _ in range(col)] for _ in range(row)]
    for x in range(row):
        for y in range(col):
            if new_arr[x][y] == -1: continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if out_bound(nx, ny, row, col): continue
                if new_arr[nx][ny] == -1: continue
                if new_arr[x][y] - new_arr[nx][ny] >= 5:
                    gap = (new_arr[x][y] - new_arr[nx][ny])//5
                    temp[x][y] -= gap
                    temp[nx][ny] += gap
                
    for i in range(row):
        for j in range(col):
            new_arr[i][j] += temp[i][j]


def flatting(maze):
    temp_arr = [[]]
    row = len(maze)
    col = len(maze[0])
    for y in range(col):
        for x in range(row-1, -1, -1):
            if maze[x][y] == -1: continue
            temp_arr[-1].append(maze[x][y])
    return temp_arr


def spread():
    four_n = n//4
    spread_arr = flatting(new_arr)
    temp = [[-1 for _ in range(four_n)] for _ in range(4)]

    for x in range(4):
        if x % 2:
            sx = four_n*x
            y = 0
            while y < four_n:
                temp[x][y] = spread_arr[-1][sx+y]
                y += 1
        else:
            y = four_n - 1
            if x == 2:
                sx = 0
            else:
                sx = four_n * 2
            
            while y >= 0:
                temp[x][y] = spread_arr[-1][sx]
                sx += 1
                y -= 1

    return temp


while check(arr[-1]):
    push()
    new_arr = roll(arr)
    blow()
    new_arr = spread()
    blow()
    arr = flatting(new_arr)
    turn += 1
print(turn)