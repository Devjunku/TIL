from collections import deque
from pprint import pprint
import sys
from tokenize import group
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
black = -1
rainbow = 0

color_g = set(range(1, m+1))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
bg = []
def is_block():
    global bg

    block_group = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 6: continue
            if not visited[i][j] and arr[i][j] != black and arr[i][j] != rainbow:
                rainbow_group = []
                group = [(i, j, arr[i][j])]
                visited[i][j] = True
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]

                        if not (0 <= nx < n and 0 <= ny < n): continue
                        if visited[nx][ny]: continue
                        if arr[nx][ny] == black: continue
                        if arr[nx][ny] == 6: continue

                        if arr[i][j] == arr[nx][ny] or arr[nx][ny] == rainbow:
                            if arr[nx][ny] == rainbow:
                                rainbow_group.append((nx, ny))
                            visited[nx][ny] = True
                            group.append((nx, ny, arr[nx][ny]))
                            q.append((nx, ny))
                print(rainbow_group)
                for s, e in rainbow_group:
                    visited[s][e] = False
                if len(group) >= 2:
                    group.sort(key=lambda x: (x[0], x[1]))
                    for r, c, v in group:
                        if v != rainbow:
                            block_group.append((len(group), r, c, group))
                            break
    
    
    block_group.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    bg = block_group
    return bg


def gravity():
    for i in range(n):
        for j in range(n-1, -1, -1):
            if arr[j][i] == black:
                continue
            x, y = j, i
            for _ in range(n-1):
                nx, ny = x+1, y
                if not (0 <= nx < n and 0 <= ny < n):
                    break
                if arr[nx][ny] == black or arr[nx][ny] in color_g or arr[nx][ny] == rainbow:
                    break
                x, y = nx, ny
            arr[j][i], arr[x][y] = arr[x][y], arr[j][i]




while is_block():
    number, r, c, bg_group = bg[0]
    pprint(bg)
    # pprint(bg[0])
    # pprint(arr)
    # print(bg_group)
    print(number, number**2)
    answer += number**2
    for x, y, v in bg_group:
        arr[x][y] = 6
    gravity()
    arr = list(map(list, zip(*arr)))[::-1]
    gravity()

print(answer)