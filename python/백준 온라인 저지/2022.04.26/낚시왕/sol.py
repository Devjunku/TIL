import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())

bowl = [[[] for _ in range(c)] for _ in range(r)]

up_down = [(-1, 0), (1, 0)]
left_down = [(0, 1), (0, -1)]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    bowl[x-1][y-1].append((z, s, d-1))


answer = 0
# TODO 1. 낚시왕이 이동한다.
for t in range(c):

    if not bowl:
        break

    # TODO 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.

    for i in range(r):
        if bowl[i][t]:
            answer += bowl[i][t][0][0]
            bowl[i][t].clear()
            break

    # TODO 3. 상어가 이동한다.
    new_bowl = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            while bowl[i][j]:
                z, s, d = bowl[i][j].pop()
                x, y = i, j
                # 위 아래이면 (열-1)*2로 나눈 몫
                if d in [0, 1]:
                    size = s % ((r-1)*2)
                    while size > 0:
                        nx, ny = x + up_down[d][0], y + up_down[d][1]
                        if not (0 <= nx < r and 0 <= ny < c):
                            d += 1
                            d %= 2
                            continue
                        x, y = nx, ny
                        size -= 1
                    new_bowl[x][y].append((z, s, d))
                # 좌 우이면 (열-1)*2로 나눈 몫
                else:
                    size = s % ((c-1)*2)    
                    d -= 2
                    while size > 0:
                        nx, ny = x + left_down[d][0], y + left_down[d][1]
                        if not (0 <= nx < r and 0 <= ny < c):
                            d += 1
                            d %= 2
                            continue
                        x, y = nx, ny
                        size -= 1
                    d += 2
                    new_bowl[x][y].append((z, s, d))


    # TODO 4. 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다.
    #  이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
    for i in range(r):
        for j in range(c):
            if new_bowl[i][j]:
                new_bowl[i][j].sort(key=lambda x: x[0])
                z, s, d = new_bowl[i][j].pop()
                new_bowl[i][j].clear()
                new_bowl[i][j].append((z, s, d))

    bowl = new_bowl[:]

print(answer)