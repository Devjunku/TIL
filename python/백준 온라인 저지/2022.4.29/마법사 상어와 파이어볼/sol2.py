import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())

fireball = []

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball.append((r, c, m, s, d))

for _ in range(k):

    new_fireball = []
    check_point = {}

    for r, c, m, s, d in fireball:
        nx, ny = (r+dx[d]*s) % n, (c+dy[d]*s) % n

        if (nx, ny) not in check_point:
            check_point[(nx, ny)] = [m, s, d, 1, d%2]
        else:
            check_point[(nx, ny)][0] += m
            check_point[(nx, ny)][1] += s
            check_point[(nx, ny)][3] += 1
            check_point[(nx, ny)][4] += d%2
    
    fireball.clear()

    for k, v in check_point.items():
        if v[3] > 1:
            if v[0] // 5 > 0:
                if v[4] == v[3] or v[4] == 0:
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 0])
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 2])
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 4])
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 6])
                else:
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 1])
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 3])
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 5])
                    new_fireball.append([k[0], k[1], v[0]//5, v[1]//v[3], 7])
        elif v[3] == 1:
            new_fireball.append([k[0], k[1], v[0], v[1], v[2]])
    
    fireball = new_fireball[:]

answer = 0
for r, c, m, s, d in fireball:
    answer += m

print(answer)
