from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cctv_d = [
    [],
    [
        [[0, 1]],
        [[1, 0]],
        [[-1, 0]],
        [[0, -1]]
    ],
    [
        [[0, 1], [0, -1]],
        [[1, 0], [-1, 0]]
    ],
    [
        [[-1, 0], [0, 1]],
        [[1, 0], [0, 1]],
        [[0, -1], [1, 0]],
        [[0, -1], [-1, 0]]
    ],
    [
        [[0, -1], [-1, 0], [0, 1]],
        [[1, 0], [0, -1], [-1, 0]],
        [[0, 1], [1, 0], [0, -1]],
        [[1, 0], [0, 1], [-1, 0]]
    ],
    [
        [[0, 1], [1, 0], [-1, 0], [0, -1]]
    ]
]

cctv = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cctv.append((i, j))
        elif arr[i][j] == 2:
            cctv.append((i, j))
        elif arr[i][j] == 3:
            cctv.append((i, j))
        elif arr[i][j] == 4:
            cctv.append((i, j))
        elif arr[i][j] == 5:
            cctv.append((i, j))

cctv_num = len(cctv)

def get_none_sight(array):
    num = 0
    for i in range(n):
        num += array[i].count(0)
    return num

answer = sys.maxsize
def get_none_sight_num(idx_cctv, mapping):
    global answer

    if idx_cctv >= cctv_num:
        # TODO 여기서 사각지대 개수 세서 update해야함
        answer = min(answer, get_none_sight(mapping))
        return
    
    sx, sy = cctv[idx_cctv]
    d = cctv_d[arr[sx][sy]]
    nxt_mapping = deepcopy(mapping)
    for direct in d:
        for _dx, _dy in direct:
            x, y = sx, sy
            while True:
                nx, ny = x + _dx, y + _dy
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                if nxt_mapping[nx][ny] == 6:
                    break
                if nxt_mapping[nx][ny] != 0 or nxt_mapping[nx][ny] == "#":
                    x, y = nx, ny
                    continue
                if nxt_mapping[nx][ny] == 0:
                    nxt_mapping[nx][ny] = "#"
            
        get_none_sight_num(idx_cctv+1, nxt_mapping)
        nxt_mapping = deepcopy(mapping)

get_none_sight_num(0, arr)
print(answer)