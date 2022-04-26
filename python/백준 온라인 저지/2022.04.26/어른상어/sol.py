from pprint import pprint
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
bowl = []
smell = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        if data[j] != 0:
            smell[i][j].append((data[j], 0))
    bowl.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark_d = [0] + list(map(int, input().split()))

shark_d_dic = {
    i: {j: [] for j in range(1, k+1)} for i in range(1, k+1)
}

for i in range(1, k+1):
    for j in range(1, k+1):
        shark_d_dic[i][j] = tuple(map(int, input().split()))


def get_shark_num():
    num = 0
    for i in range(n):
        for j in range(n):
            if bowl[i][j] != 0:
                num += 1
            if num > 1:
                return True
    
    return False

t = 0
while get_shark_num():

    if t > 1000:
        print(-1)
        exit()

    new_bowl = [[0 for _ in range(n)] for _ in range(n)]

    # TODO 상어 이동
    for i in range(n):
        for j in range(n):
            # TODO FIRST 인접한 칸 중에서 아무 냄새가 없는 칸으로 감 우선순위대로 움직임
            if bowl[i][j]:
                shark_num, shark_d_num = bowl[i][j], shark_d[bowl[i][j]]
                x, y = i, j
                find_blank = False
                for d_i in shark_d_dic[shark_num[shark_d_num]]:
                    nx, ny = x + dx[d_i-1], y  + dy[d_i-1]
                    if not (0 <= nx < n and 0 <= ny < n): continue
                    
                    if bowl[nx][ny] == 0:
                        find_blank = True
                        new_bowl[nx][ny] = shark_num
                        shark_d[bowl[i][j]] = d_i
                        break
                
                if not find_blank:
                    for d_i in shark_d_dic[shark_num[shark_d_num]]:
                        nx, ny = x + dx[d_i-1], y  + dy[d_i-1]
                        if not (0 <= nx < n and 0 <= ny < n): continue
                        if smell[nx][ny]:
                            if smell[nx][ny][0] == shark_num:
                                find_blank = True
                                new_bowl[nx][ny] = shark_num
                                shark_d[bowl[i][j]] = d_i
                                break
                    
            # 그런 칸이 없으면 자신의 냄새가 있는 칸으로 감
    t += 1

    pass

