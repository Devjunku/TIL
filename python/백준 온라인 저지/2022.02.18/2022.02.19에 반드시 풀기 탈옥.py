import sys
from collections import deque
input = sys.stdin.readline

TEST_CASE = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def find_load(x, y):
    








    return


for _ in range(TEST_CASE):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]

    prisoner = []
    door_dic = {}
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "$":
                prisoner.append((i, j))
            if arr[i][j] == "#":
                door_dic[(i, j)] = False

    res = 0
    h_num = 0
    for x, y in prisoner:

        
    
 

