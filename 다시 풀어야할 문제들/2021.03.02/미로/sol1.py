import sys

sys.stdin = open('sample_input.txt')

dy = [-1, 1, 0, 0] # 방향설정
dx = [0, 0, -1, 1]

def start_end(maze): # 출발점 찾기
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                return y, x # 찾자마자 리턴

def safe(y, x): # 범위에 벗어나지 않거나, 1이 아닌지(벽이 아닌지)
    if 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3):
        return True # 조건에 맞다면 True
    else:
        return False # 그렇지 않다면, False

def dfs(y, x):
    global res

    if maze[y][x] == 3: # 3이 뜬다면 True
        res = 1
        return # 그냥 return으로 None을 반환하되 global 변수인 res를 통제하여 print 할 수 있도록

    visited.append((y, x)) # 들어온 좌표를 튜플형태로 원소 추가
    for k in range(4): # 방향을 정하면서
        n_x = x + dx[k] # 더해줌
        n_y = y + dy[k] # 더해줌
        if safe(n_y, n_x) and (n_y, n_x) not in visited: # 방문하지도 않았으면서 범위에 벗어나지 않았으면
            dfs(n_y, n_x) # 재귀로 돎


T = int(input())
for t in range(1, T+1):
    N = int(input())

    maze = [] # 데이터 받기
    for _ in range(N):
        maze.append(list(map(int, list(input()))))
    # print(maze)

    visited = []
    res = 0
    y, x = start_end(maze) # 출발점 지정
    # print(y, x)
    dfs(y, x) # dfs 탐색 시작
    print('#{} {}'.format(t, res))
