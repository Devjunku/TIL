import sys

input = sys.stdin.readline

n = int(input())
room_horizon = [list(input()) for _ in range(n)]
room_vertical = list(map(list, zip(*room_horizon)))

seq = 0
horizon_num = 0
for i in range(n):
    for j in range(n):
        if room_horizon[i][j] == ".":
            seq += 1
            if seq >= 2:
                horizon_num += 1
                sep = 0
                break
        else:
            seq = 0



seq = 0
vertical_num = 0
for i in range(n):
    for j in range(n):
        if room_vertical[i][j] == ".":
            seq += 1
            if seq >= 2:
                vertical_num += 1
                seq = 0
                break
        else:
            seq = 0

print(f"{horizon_num} {vertical_num}")