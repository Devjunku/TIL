"""
1. a에 지도를 입력한다. 상어가 있는 좌표에서는 a[i][j]를  [상어의 크기, k] 로 바꿔준다
   shark에는 인덱스와 상어의 크기를 맞춰서 상어의 좌표를 저장한다
2. shark에 상어의 처음 방향을 순서대로 append한다
3. dir에 각 상어의 방향 우선순위를 순서대로 저장한다
4. 상어가 조건대로 계속 이동한다. 만약 ans가 1001이면 -1을 출력하고 끝낸다
   상어 좌표가 중복되는지 검사할 리스트 check를 만든다
5. shark에 저장된 좌표를 순서대로 불러온다
   방향 우선순위에 맞춰서 다음 칸이 빈칸이면 flag를 1로 두고 break한다
6. 사방에 냄새가 있으면 다시 방향 우선순위에 맞춰서 자신의 크기와 같은 값을 가진 칸을 찾는다
7. 만약 check[nx][ny]에 이미 값이 있고 i+1보다 작다면 현재 상어를 없앤다
   반대의 경우에는 이미 자리잡고 있던 상어를 없앤다
8. check[nx][ny]가 빈칸이면 현재 이동할 상어의 크기를 저장하고 shark[i]를 새로운 좌표와 방향으로 갱신한다 
9. a의 좌표를 하나씩 불러와서 값이 있으면 냄새에 1을 빼준다. 냄새가 0이 되면 그 칸을 0으로 리셋한다
10. shark에 저장된 좌표를 하나씩 불러와서 a에 상어가 있는 좌표의 정보를 갱신한다
11. shark에 0이 m-1개 있으면 1번째 상어만 있는 것이므로 걸린 시간을 출력하고 끝낸다
"""


import sys
input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
a, shark = [], [[] for _ in range(m)]

for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j]:
            shark[a[i][j]-1].extend([i,j])
            a[i][j] = [a[i][j], k]

d = list(map(int, input().split()))
for i in range(m):
    shark[i].append(d[i])

dir = [[] for _ in range(m)]
idx = -1
for i in range(4*m):
    if i % 4 == 0:
        idx += 1
    dir[idx].append(list(map(int, input().split())))

ans = 0
while True:
    ans += 1
    if ans == 1001:
        print(-1)
        break

    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        if shark[i] != 0:
            x, y, d, flag = shark[i][0], shark[i][1], shark[i][2], 0
            for j in range(4):
                ndir = dir[i][d-1][j]
                nx, ny = x + dx[ndir] , y + dy[ndir]
                if 0 <= nx < n and 0 <=  ny < n:
                    if a[nx][ny] == 0:
                        flag = 1
                        break
            
            if flag == 0:
                for j in range(4):
                    ndir = dir[i][d-1][j]
                    nx, ny = x + dx[ndir], y + dy[ndir]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny][0] == i + 1:
                            break
            
            if check[nx][ny]:
                if check[nx][ny] < i + 1:
                    shark[i] = 0
                else:
                    shark[check[nx][ny]-1] = 0
            else:
                check[nx][ny] = i + 1
                shark[i] = [nx, ny, ndir]
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                a[i][j][1] -= 1
                if a[i][j][1] == 0:
                    a[i][j] = 0
    
    for i in range(m):
        if shark[i]:
            x, y = shark[i][0], shark[i][1]
            a[x][y] = [i+1, k]
    
    if shark.count(0) == m-1:
        print(ans)
        break

