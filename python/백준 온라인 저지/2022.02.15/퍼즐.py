import sys
from collections import deque
input = sys.stdin.readline

arr = []
hash_key = ""
for _ in range(3):
    ele = list(map(int, input().split()))
    hash_key += "".join(list(map(str, ele)))


def bfs():
    queue = deque([(hash_key, 0)])
    visit = {
        hash_key: True
    }

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        key, cnt = queue.popleft()

        if key == "123456780":
            return cnt

        zero = key.index("0")
        row = zero // 3
        col = zero % 3

        for i in range(4):
            nrow, ncol = row + dx[i], col + dy[i]
            if 0 <= nrow < 3 and 0 <= ncol < 3: 
                key_list = list(key)
                key_list[zero], key_list[3 * nrow + ncol] = key_list[3 * nrow + ncol], key_list[zero]
                new_key = "".join(key_list)
                if new_key in visit.keys():
                    continue
                else:
                    visit[new_key] = True
                    queue.append((new_key, cnt + 1))
    return -1

print(bfs())