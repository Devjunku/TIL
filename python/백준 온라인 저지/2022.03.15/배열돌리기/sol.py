import sys
from copy import deepcopy
from itertools import permutations
input = sys.stdin.readline

n, m, k = map(int, input().split())

origin_arr =  [list(map(int, input().split())) for _ in range(n)]
k_list = []
for _  in range(k):
    k_list.append(tuple(map(int, input().split())))

k_idx = [i for i in range(k)]
p_k_idx = permutations(k_idx, k)

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

answer = int(1e9)
for element in p_k_idx:
    arr = deepcopy(origin_arr)
    for idx in element:
        r, c, s = k_list[idx][0], k_list[idx][1], k_list[idx][2]
        left_top_x, left_top_y = r-s-1, c-s-1
        right_bottom_x, right_bottom_y = r+s-1, c+s-1

        r = deepcopy(left_top_x)
        c = deepcopy(left_top_y)

        pivot = 0
        
        new_arr = [[0 for _ in range(m)] for _ in range(n)]
        dx, dy = 0, 0
        while left_top_x != right_bottom_x and left_top_y != right_bottom_y:
            if pivot%4 == 0 and c == right_bottom_y:
                pivot += 1
            elif pivot%4 == 1 and r == right_bottom_x:
                pivot += 1
            elif pivot%4 == 2 and c == left_top_y:
                pivot += 1
            elif pivot%4 == 3 and r == left_top_x:
                pivot += 1
                left_top_x += 1
                left_top_y += 1
                right_bottom_x -= 1
                right_bottom_y -= 1
                r = left_top_x
                c = left_top_y
            dx, dy = direct[pivot%4]
            if left_top_x <= r + dx <= right_bottom_x and left_top_y <= c + dy <= right_bottom_y:
                new_arr[r+dx][c+dy] = arr[r][c]
                r += dx 
                c += dy

        for i in range(n):
            for j in range(m):
                if new_arr[i][j] != 0:
                    arr[i][j] = new_arr[i][j]
    
    for i in range(n):
        answer = min(sum(arr[i]), answer)

print(answer)