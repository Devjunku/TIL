import sys
input = sys.stdin.readline

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

clouds = [
    (n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)
]

diag_x = [1, -1, 1, -1]
diag_y = [1, 1, -1, -1]

for _ in range(m):
    d, s = map(int, input().split())
    move_loc = {}

    # TODO 1, 2, 3
    while clouds:
        x, y = clouds.pop()
        nx, ny = (x + dx[d-1]*s)%n, (y+dy[d-1]*s)%n
        arr[nx][ny] += 1
        move_loc[(nx, ny)] = arr[nx][ny]

    # TODO 4
    for key, value in move_loc.items():
        basket = 0
        for i in range(4):
            nx, ny = key[0] + diag_x[i], key[1] + diag_y[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if arr[nx][ny] > 0:
                basket += 1
        
        arr[key[0]][key[1]] += basket

    # TODO 5
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2:
                if (i, j) not in move_loc.keys():
                    clouds.append((i, j))
                    arr[i][j] -= 2

ans = 0
for i in range(n):
    ans += sum(arr[i])

print(ans)