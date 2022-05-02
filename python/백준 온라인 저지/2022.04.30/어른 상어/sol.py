import sys
from pprint import pprint
input = sys.stdin.readline

n, m, k = map(int, input().split())

smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
bowl = [list(map(int, input().split())) for _ in range(n)]
shark_d = [0] + list(map(int, input().split()))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

shark_d_did = {
    i: {
        j:list(map(int, input().split())) for j in range(1, 5)
    } for i in range(1, m+1)
}

for i in range(n):
    for j in range(n):
        if bowl[i][j] != 0:
            smell[i][j][0] = k
            smell[i][j][1] = bowl[i][j]

def confirm():

    for i in range(n):
        for j in range(n):
            if bowl[i][j] > 1:
                return True
    
    return False

t = 0
while confirm():
    if t >= 1000:
        print(-1)
        exit()
    
    # TODO 냄새 1씩 감소
    for i in range(n):
        for j in range(n):
            if smell[i][j][0] > 0:
                smell[i][j][0] -= 1
            
            if smell[i][j][0] == 0:
                smell[i][j][1] = 0
    
    # TODO 상어 이동
    new_bowl = [[401 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if bowl[i][j] != 0:
                shark_number = bowl[i][j]
                shark_direct = shark_d[shark_number]
                x, y = i, j
                flag = True
                smell[i][j][0] = k
                smell[i][j][1] = bowl[i][j]
                # 빈 격자로 가기
                for d in shark_d_did[shark_number][shark_direct]:
                    nx, ny = x + dx[d], y + dy[d]
                    # 격자 밖 안됨
                    if not (0 <= nx < n and 0 <= ny < n): continue
                    # 냄새가 있음 안됨
                    if smell[nx][ny][0] > 0: continue
                    # 빈 칸이면
                    if bowl[nx][ny] == 0:
                        flag = False
                        if bowl[i][j] < new_bowl[nx][ny]:
                            new_bowl[nx][ny] = bowl[i][j]
                            shark_d[shark_number] = d
                            break
                        else:
                            break
                # 내 냄새 나는 칸으로 가기
                if flag:
                    for d in shark_d_did[shark_number][shark_direct]:
                        nx, ny = x + dx[d], y + dy[d]
                        # 격자 밖 안됨
                        if not (0 <= nx < n and 0 <= ny < n): continue
                        # 내 냄새가 나는 칸이면
                        if smell[nx][ny][1] == bowl[i][j]:
                            new_bowl[nx][ny] = bowl[i][j]
                            shark_d[shark_number] = d
                            break
    
    for i in range(n):
        for j in range(n):
            if new_bowl[i][j] == 401:
                new_bowl[i][j] = 0   

    bowl = new_bowl[:]

    t += 1

print(t)
