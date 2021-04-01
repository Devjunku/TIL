from pandas import DataFrame
from collections import deque

T = int(input()) # 테스트 케이스 갯수

# 델타 이동
dx = [2, 2, 1, 1, -1, -1, -2, -2] 
dy = [1, -1, 2, -2, -2, 2, -1, 1]


# 안전 좌표 확인
def safe(x, y, I):
    if 0 <= x < I and 0 <= y < I:
        return True
    return False

# bfs
def bfs(sx, sy):
    global dx, dy, I, arr, ex, ey, queue, go, cnt

    queue.append((sx, sy))
    nx, ny = queue[0]
    arr[nx][ny] = 1
    
    if nx == ex and ny == ey: # 시작점과 끝점이 갖다면 바로 리턴
        return 1

    while queue:
        x, y = queue.popleft()
        stack = deque((x, y))
        while stack:
            x, y = stack.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if not safe(nx, ny, I) or arr[nx][ny] == 1:
                    continue
                arr[nx][ny] = 1
                stack.append((nx, ny))
        queue.append(stack)
        

        print(DataFrame(arr))



for t in range(1, T+1):
    I = int(input())
    arr = [[0 for _ in range(I)] for _ in range(I)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    arr[sx][sy] = 1 # 시작점
    arr[ex][ey] = 1 # 끝점
    queue = deque() # 큐 할당
    cnt = 0 # 이동 칸 세기
    go = 0 #
    # print(DataFrame(arr))
    bfs(sx, sy)



    
