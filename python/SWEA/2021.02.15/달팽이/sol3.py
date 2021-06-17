from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())




def solution(N):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    number = 1
    x = y = 0
    idx_move = +1

    for i in range(N, 0, -1):
        if i == 1:
            matrix[y][x] = number
        else:
            for k in range(i):
                matrix[y][x] = number
                number += 1
                if k == i - 1:
                    y += idx_move
                else:
                    x += idx_move

            for k in range(i - 1):
                matrix[y][x] = number
                number += 1
                if k == i - 2:
                    idx_move *= -1
                    x += idx_move
                else:
                    y += idx_move
    return matrix

for t in range(1, T+1):
    N = int(input())
    dat = solution(N)

    print('#{}'.format(t))
    for i in range(len(dat)):
        print(*dat[i])