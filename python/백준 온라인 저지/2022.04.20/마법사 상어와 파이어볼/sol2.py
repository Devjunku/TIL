import sys
input = sys.stdin.readline

n, m, count = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(m)]

direct = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
cnt = 0

while True:
    check = {}
    new_fireball = []

    for r, c, m, s, d in fireball:
        dx, dy = s * direct[d][0], s * direct[d][1]
        new_r, new_c = (r+dx)%n, (c+dy)%n

        if (new_r, new_c) not in check:
            check[(new_r, new_c)] = [m, s, d, 1, d % 2]
        else:
            check[(new_r, new_c)][0] += m
            check[(new_r, new_c)][1] += s
            check[(new_r, new_c)][3] += 1
            check[(new_r, new_c)][4] += d % 2
    
    for k, v in check.items():
        if v[3] == 1:
            new_fireball.append([k[0], k[1], v[0], v[1], v[2]])
        
        else:
            if not v[0] // 5 == 0:
                if v[4] == 0 or v[3] == v[4]:
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 0])
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 2])
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 4])
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 6])
                else:
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 1])
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 3])
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 5])
                    new_fireball.append([k[0], k[1], v[0] // 5, v[1] // v[3], 7])
    
    fireball = new_fireball[:]
    cnt += 1

    if cnt >= count:
        break

res = 0

for r, c, m, s, d in fireball:
    res += m

print(res)