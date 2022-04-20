import sys
input = sys.stdin.readline

n = int(input())
sand = [list(map(int, input().split())) for _ in range(n)]
sx, sy = n//2, n//2

left = [
    (1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
    (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)
]

right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
ans = 0

def recount_sand(time, dx, dy, direction):
    global sx, sy, ans

    for _ in range(time):
        sx += dx
        sy += dy

        if sy < 0:
            break

        total = 0

        for dx, dy, z in direction:
            nx, ny = sx + dx, sy + dy
            
            if z == 0:
                new_sand = sand[sx][sy]- total
            else:
                new_sand = int(sand[sx][sy] * z)
                total += new_sand
            
            if 0 <= nx < n and 0 <= ny < n:
                sand[nx][ny] += new_sand
            else:
                ans += new_sand

for i in range(1, n+1):
    if i % 2:
        recount_sand(i, 0, -1, left)
        recount_sand(i, 1, 0, down)
    else:
        recount_sand(i, 0, 1, right)
        recount_sand(i, -1, 0, up)

print(ans)