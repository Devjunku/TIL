from copy import deepcopy
from pprint import pprint
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

t = 0

while t < k:
    # TODO 1 파이어볼 이동
    new_arr = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            while arr[i][j]:
                x, y = i, j
                m, s, d = arr[i][j].pop()
                for _ in range(1, int(s+1)):
                    nx, ny = x + dx[d], y + dy[d]
                    x, y = nx % n, ny % n
                
                new_arr[x][y].append([m, s, d])

    # TODO 2개 이상의 파이어볼이 있는 칸 확인
    distri_arr = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 하나로 합치기 위해 2개 이상 확인
            total = len(new_arr[i][j])
            all_even_odd = []
            if total >= 2:
                sum_new_m, sum_new_s, sum_new_d = 0, 0, 0
                for new_m, new_s, new_d in new_arr[i][j]:
                    sum_new_m += new_m
                    sum_new_s += new_s
                    if new_d % 2 == 0: all_even_odd.append(1)
                    else: all_even_odd.append(0)
                
                n_m = (sum_new_m) // 5
                # 질량이 0인지 확인
                if n_m == 0: continue

                n_s = (sum_new_s) // total
                toggle = sum(all_even_odd)
                # 모두 홀수이거나 모두 짝수인지 확인
                if toggle == total or toggle == 0: n_d = [0, 2, 4, 6]
                else: n_d = [1, 3, 5, 7]

                for nd in n_d: distri_arr[i][j].append([n_m, n_s, nd])

            else:
                for fireball in new_arr[i][j]:
                    distri_arr[i][j].append(fireball)
    arr = deepcopy(distri_arr)
    t += 1

ans = 0
for i in range(n):
    for j in range(n):
        while arr[i][j]:
            m, s, d = arr[i][j].pop()
            ans += m

print(ans)