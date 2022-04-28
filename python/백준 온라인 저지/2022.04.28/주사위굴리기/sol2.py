from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 2, 3, 4, 5, 6]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, dir, score = 0, 0, 0, 0

def bfs(x, y, number):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    q = deque([(x, y)])
    cnt = 1

    while q:
        sx, sy = q.popleft()
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if not (0 <= nx < n and 0 <= ny < m): continue
            if not visited[nx][ny] and (arr[nx][ny] == number):
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
    
    return cnt * number

for _ in range(k):

    for i in range(4):
        nx, ny = x + dx[dir], y + dy[dir]

        if not (0 <= nx < n and 0 <= ny < m):
            dir = (dir+2) % 4
            nx, ny = x + dx[dir], y + dy[dir]

    x, y = nx, ny
    score += bfs(x, y, arr[x][y])

    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif dir == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    if dice[5] > arr[x][y]:
        dir = (dir+1) % 4
    elif dice[5] < arr[x][y]:
        dir = (dir+3) % 4

print(score)