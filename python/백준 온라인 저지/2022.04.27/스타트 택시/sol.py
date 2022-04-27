from collections import deque
import sys
input = sys.stdin.readline

n, m, volume = map(int, input().split())
mapping = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
person = [[0 for _ in range(n)] for _ in range(n)]
desination = [[set() for _ in range(n)] for _ in range(n)]

for i in range(1, m+1):
    psx, psy, dex, dey = map(int, input().split())
    person[psx-1][psy-1] = i
    desination[dex-1][dey-1].add(i)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def confirm_person():

    for i in range(n):
        for j in range(n):
            if person[i][j] != 0:
                return True
    
    return False

def find_person(sx, sy):
    if person[sx][sy] != 0:
        return (0, sx, sy, person[sx][sy])

    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    result = []
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny]: continue
            if mapping[nx][ny] == 1: continue
            if person[nx][ny] != 0: 
                result.append((cost+1, nx, ny, person[nx][ny]))
            visited[nx][ny] = True
            q.append((nx, ny, cost+1))
    if not result:
        return None, None, None, None
    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return result[0]

def find_destination(sx, sy, number):

    if number in desination[sx][sy]:
        return (0, sx, sy)

    visited = [[False for _ in range(n)] for _ in range(n)]

    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True

    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny]: continue
            if mapping[nx][ny] == 1: continue
            if number in desination[nx][ny]:
                return (cost+1, nx, ny)
            visited[nx][ny] = True
            q.append((nx, ny, cost+1))
    
    return None, None, None

while confirm_person():

    # TODO 현재 위치에서 person 찾기 -> 거리, 행, 열로 뽑기
    start_useage, pr, pc, number = find_person(sx, sy)
    if start_useage == None:
        print(-1)
        exit()
    sx, sy = pr, pc
    # TODO 갈 수 없으면 -1 출력하고 빠져나와버림
    if volume-start_useage < 0:
        print(-1)
        exit()
    volume -= start_useage
    # TODO 태운 승객의 경우 0으로 표시
    person[pr][pc] = 0

    # TODO 이 승객에서 목적지를 찾기 위한 bfs시작
    end_useage, dr, dc = find_destination(sx, sy, number)
    if end_useage == None:
        print(-1)
        exit()
    sx, sy = dr, dc
    # TODO 갈 수 없으면 -1 출력하고 빠져나오기
    if volume-end_useage < 0:
        print(-1)
        exit()
    volume -= end_useage
    volume += (end_useage*2)

print(volume)