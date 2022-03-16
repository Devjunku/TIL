import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
fishbowl = [list(map(int, input().split())) for _ in range(n)]

shark_weight = 2
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if fishbowl[i][j] == 9:
            shark_r = i
            shark_c = j
            break


def can_go(shark_weight, r, c):

    q = deque([])
    q.append((r, c, 0))
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[r][c] = True
    # 먹이의 거리와 위치를 담을 배열
    can_eat_list = []
    while q:
        cx, cy, dist = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            # 경계안에 있다면
            if 0 <= nx < n and 0 <= ny < n:
                # 방문 했니?
                if not visited[nx][ny]:
                    # 0이면 그냥 queue에 넣고 거리만 증가
                    if fishbowl[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny, dist+1))
                    else:
                        # 그렇지 않으면 상어 크기랑 물고기 크기로 판별
                        # 크다면? 먹이의 거리와 위치 배열에 담음
                        if fishbowl[nx][ny] < shark_weight:
                            can_eat_list.append((dist+1, nx , ny))
                            visited[nx][ny] = True
                            q.append((nx, ny, dist+ 1))
                        # 같다면 그냥 지나감 → 사실 이 코드는 위에서 처리할 수 있음
                        elif fishbowl[nx][ny] == shark_weight:
                            visited[nx][ny] = True
                            q.append((nx, ny, dist + 1))

    can_eat_list.sort(key=lambda x: (x[0], x[1], x[2]))

    if can_eat_list:
        return can_eat_list[0]
    else:
        return None

# 답
t = 0
# 상어 weight 조정
eat_cnt = 0
while True:

    result = can_go(shark_weight, shark_r, shark_c)
    if result == None:
        print(t)
        break
    
    # 이동한 거리가 곧 시간
    t += result[0]

    # 먹은 갯수 만큼 count
    eat_cnt += 1
    if shark_weight == eat_cnt:
        eat_cnt = 0
        shark_weight += 1

    # 상어가 이동했기 때문에 원래 위치는 아무것도 없고 먹은 위치는 0으로 놔주어야 함
    fishbowl[shark_r][shark_c] = 0
    fishbowl[result[1]][result[2]] = 0
    
    # 상어 위치 업데이트
    shark_r, shark_c = result[1], result[2]