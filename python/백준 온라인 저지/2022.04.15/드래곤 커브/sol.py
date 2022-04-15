import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
mapping = [[0 for _ in range(101)] for _ in range(101)]

def dragon_curve(x, y, d, g):

    mapping[x][y] = 1
    init_d = [d]
    for j in range(g):
        """
        TODO 다음 세대 방향을 결정해야 한다.
        다음 세대의 새로운 부분은 원래 세대 방향을 반대로 정렬한 다음, 90도 회전시킨것과 같다.
        """
        if j >= 1:
            init_d = []
            for dr in dragon_d:
                init_d.extend(dr)
        init_d.reverse()
        for i in range(len(init_d)):
            init_d[i] += 1
            init_d[i] %= 4
        # TODO 세대 방향을 넣어준다.
        dragon_d.append(deepcopy(init_d))
        
    return

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# → , ↑ , ← , ↓

for _ in range(n):
    x, y, d, g = map(int, input().split())
    dragon_d = [[d]]
    mapping[y][x] = 1
    dragon_curve(x, y, d, g)
    # print(dragon_d)
    sx, sy = x, y
    for generation in dragon_d:
        for direct in generation:
            nx, ny  = sx + dx[direct], sy + dy[direct]
            # print(nx, ny)
            if not (0 <= nx <= 100 and 0 <= ny <= 100):
                sx, sy = nx, ny
                continue
            mapping[ny][nx] = 1
            sx, sy = nx, ny

cnt = 0
for i in range(100):
    for j in range(100):
        if mapping[i][j] == 1 and mapping[i+1][j] == 1 and mapping[i][j+1] == 1 and mapping[i+1][j+1] == 1:
            cnt += 1

print(cnt)