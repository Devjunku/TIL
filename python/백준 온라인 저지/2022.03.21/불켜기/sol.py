from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

room_switch = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    room_switch[x][y].append((a, b))
# pprint(room_switch)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):

    q = deque([])
    q.append((x, y))

    turnOn_room = [[False for _ in range(n+1)] for _ in range(n+1)]
    turnOn_room[x][y] = True
    visited = [[False for _ in range(n+1)] for _ in range(n+1)] 
    visited[x][y] = True

    cnt = 1
    while q:

        cx, cy = q.popleft()
        # 현재 위치에서 불 다키기
        for turn_right, turn_left in room_switch[cx][cy]:
            if not turnOn_room[turn_right][turn_left]:
                turnOn_room[turn_right][turn_left] = True
                cnt += 1
                # 불이 켜진 장소에서 상 하 좌 우 중 방문했었던 적이 있다면 그 방문한 곳을 q에 넣는다.
                for i in range(4):
                    nx = turn_right + dx[i]
                    ny = turn_left + dy[i]
                    if not (0 < nx <= n and 0 < ny <= n):
                        continue
                    if visited[nx][ny]:
                        q.append((nx, ny))
        
        # 4방향을 돌면서 불이 켜져있지만, 방문하지 않았던 곳을 q에 넣는다.
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 < nx <= n and 0 < ny <= n): continue
            if not visited[nx][ny] and turnOn_room[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    return cnt

print(bfs(1, 1))