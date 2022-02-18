import sys
from pprint import pprint
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n, m, k = map(int, input().split())
shark_init = [list(map(int, input().split())) for _ in range(n)]
shark_smell = [[0 for _ in range(n)] for _ in range(n)]

shark_l = []

for i in range(n):
    for j in range(n):
        if shark_init[i][j] != 0:
            shark_smell[i][j] = k
            shark_l.append((i, j))

to_direct = {
    1: "up",
    2: "down",
    3: "left",
    4: "right"
}

shark_init_direct = {
    idx+1: value for idx, value in enumerate(list(map(int, input().split())))
}

shark_direct = {i: {
    to_direct[j+1]: list(map(int, input().split())) for j in range(4)
    } for i in range(1, m+1)
}

def remove_smell():
    for i in range(n):
        for j in range(n):
            if shark_smell == 0:
                pass
            else:
                shark_smell[i][j] -= 1


def move_shark(shark_list):
    pass


t = 0
while t <= 1000:
    t += 1

    # 상어 이동 | 초기 방향에 따라 이동
    # 이때 인접칸 중 아무런 냄새가 없는 곳으로 감
    # 냄새가 있으면 방향에 따른 우선순위로 반영하도록 함
    # 겹치면 상어 번호에 따라 없애버림
    #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   