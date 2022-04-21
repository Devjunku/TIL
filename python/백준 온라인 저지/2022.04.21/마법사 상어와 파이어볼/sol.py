import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(m)]

direct = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

cnt = 0

while True:

    check = {}
    new_fireball = []

    for r, c, m, s, d in fireball:
        dx, dy = direct[d][0] * s, direct[d][1] * s
        nx, ny = (r + dx) % n, (c + dy) % n

        if (nx, ny) not in check:
            check[(nx, ny)] = [m, s, d, 1, d%2]
        else:
            check[(nx, ny)][0] += m
            check[(nx, ny)][1] += s
            check[(nx, ny)][3] += 1
            check[(nx, ny)][4] += d%2
    
    for key, value in check.items():
        if value[3] == 1:
            new_fireball.append([key[0], key[1], value[0], value[1], value[2]])
        else:
            if value[0]//5 != 0:
                if value[3] == value[4] or value[4] == 0:
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 0])
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 2])
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 4])
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 6])
                else:
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 1])
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 3])
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 5])
                    new_fireball.append([key[0], key[1], value[0]//5, value[1]//value[3], 7])

    fireball = new_fireball[:]
    cnt+= 1

    if cnt >= k:
        break

ans = 0
for r, c, m, s, d in fireball:
    ans += m

print(ans)