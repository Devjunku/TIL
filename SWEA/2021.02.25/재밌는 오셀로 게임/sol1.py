from pandas import DataFrame

import sys

sys.stdin = open('sample_input.txt')




def dontgo(N, arr, x, y, color):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    if arr[x][y] == 0:
        return 0
    if arr[x][y] == color:
        return 2
    return 1

# 방향 설정
d_x = [0, 0, 1, -1, 1, 1, -1, -1]
d_y = [1, -1, 0, 0, 1, -1, 1, -1]

def solution(arr, d_x, d_y, x, y, color):
    for i in range(8):
        margin_x = d_x[i]
        margin_y = d_y[i]
        exchange = []
        while True:
            deter = dontgo(N, arr, x+margin_x, y+margin_y, color)
            if deter == 0:
                break
            if deter == 2:
                for e_x, e_y in exchange:
                    arr[e_x][e_y] = color
                break
            if deter == 1:
                exchange.append([x+margin_x, y+margin_y])
            margin_x += d_x[i]
            margin_y += d_y[i]
    arr[x][y] = color
    return arr


T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    half = N // 2
    arr[half-1][half-1] = 2
    arr[half][half] =2
    arr[half-1][half] = 1
    arr[half][half-1] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        arr = solution(arr, d_x, d_y, x-1, y-1, color)
    w = 0
    b = 0
    for line in arr:
        w += line.count(1)
        b += line.count(2)
    print('#{} {} {}'.format(t, w, b))





