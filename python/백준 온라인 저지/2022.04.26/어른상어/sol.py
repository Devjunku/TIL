from copy import deepcopy
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

bowl = [list(map(int, input().split())) for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# TODO 초기 냄새 기록
def memo_smell():
    for i in range(n):
        for j in range(n):
            if bowl[i][j] != 0:
                smell[i][j][0] = k
                smell[i][j][1] = bowl[i][j]

def mius_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][0] > 0:
                smell[i][j][0] -= 1

            if smell[i][j][0] == 0:
                smell[i][j][1] = 0

shark_d = [0] + list(map(int, input().split()))

p_shark_d = {
    i:{
        j: [] for j in range(1, 5)
    } for i in range(1, m+1)
}

for i in range(1, m+1):
    for j in range(1, 5):
        p_shark_d[i][j] = list(map(int, input().split()))

def comfirm():
    for i in range(n):
        for j in range(n):
            if bowl[i][j] > 1:
                return True

    return False

t = 0
memo_smell()
while comfirm():

    if t > 999:
        print(-1)
        exit()

    # TODO 상어 이동!
    new_bowl = [[401 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if bowl[i][j] > 0:
                shark_number = bowl[i][j]
                shark_direction = shark_d[shark_number]
                x, y = i, j
                flag = True
                # TODO 빈칸을 먼저 찾기
                for d in p_shark_d[shark_number][shark_direction]:
                    nx, ny = x + dx[d], y + dy[d]
                    if not (0 <= nx < n and 0 <= ny < n): continue
                    if smell[nx][ny][0]: continue
                    if bowl[nx][ny] == 0 and (shark_number < new_bowl[nx][ny]):
                        # print(shark_number)
                        new_bowl[nx][ny] = shark_number
                        shark_d[shark_number] = d
                        flag = False
                        break
                    elif bowl[nx][ny] == 0 and (shark_number > new_bowl[nx][ny]):
                        flag = False
                        break
                if flag:
                    for d in p_shark_d[shark_number][shark_direction]:
                        nx, ny = x + dx[d], y + dy[d]
                        if not (0 <= nx < n and 0 <= ny < n): continue
                        # TODO 자기 냄새인것 찾기
                        if smell[nx][ny][1] == bowl[i][j]:
                            new_bowl[nx][ny] = bowl[i][j]
                            shark_d[shark_number] = d
                            break
    
    for i in range(n):
        for j in range(n):
            if new_bowl[i][j] == 401:
                new_bowl[i][j] = 0
    
    bowl = deepcopy(new_bowl)

    # TODO 냄새 1씩 빼기
    mius_smell()
    # TODO 냄새기록하기
    memo_smell()
    t += 1

print(t)