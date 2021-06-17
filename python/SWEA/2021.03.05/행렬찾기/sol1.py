import sys

sys.stdin = open('input.txt')


def sort_2dimen(col_row):
    for i in range(0, len(col_row)-1):
        for j in range(i+1, len(col_row)):
            if col_row[i][0] * col_row[i][1] > col_row[j][0] * col_row[j][1]:
                col_row[j], col_row[i] = col_row[i], col_row[j]
            elif col_row[i][0] * col_row[i][1] == col_row[j][0] * col_row[j][1]:
                if col_row[i][0] > col_row[j][0]:
                    col_row[j], col_row[i] = col_row[i], col_row[j]
    return col_row

def safe(y, x):
    if y >= n or y < 0 or x >= n or x < 0:
        return False
    else:
        if arr[y][x] == 0:
            return False
    return True

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def BFS(y, x):
    global dy, dx, arr
    queue = []
    queue.append((y, x))
    c = 0
    r = 0
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not safe(ny, nx):
                continue
            else:
                arr[ny][nx] = 0
                queue.append((ny, nx))
                if c < ny:
                    c = ny
                if r < nx:
                    r = nx
    return r, c

def nums_rac(arr): # 여기서 arr 돌리면서 BFS 해줄거임 cnt도 해주고
    global cnt
    col_row = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                continue
            elif arr[i][j] >= 1:
                c, r = BFS(i, j)
                cnt += 1 # BFS 끝나면 cnt 해주기!
                col_row.append([r+1-i, c+1-j])
    return cnt, col_row

T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    cnt = 0
    cnt_res, col_row = nums_rac(arr)
    print('#{} {}'.format(t, cnt_res), end = ' ')
    for i in sort_2dimen(col_row):
        print(*i, end =' ')
    print()


