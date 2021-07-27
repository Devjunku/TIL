# 시간초과... ㅠ
import sys

N = int(input())
N_list = list(map(int, input().split()))
res_list = [0 for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        dif = abs(N_list[i]-N_list[j])
        res_list[i] += dif
        res_list[j] += dif

idx_num = 0
min_num = sys.maxsize
for num, su in zip(N_list, res_list):
    if su < min_num:
        min_num = su
        idx_num = num
    elif su == min_num:
        idx_num = num

print(idx_num)