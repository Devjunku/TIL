import sys
input = sys.stdin.readline

def manhaton(sx, sy, ex, ey): return abs(ex - sx) + abs(ey - sy)


n = int(input())
sx, sy, ex, ey = map(int, input().split())
answer = []

distance = sys.maxsize
for i in range(1, n+1):

    m = int(input())
    mid_point = []
    
    for _ in range(m): mid_point.append(tuple(map(int, input().split())))

    value = 0
    value += manhaton(sx, sy, mid_point[0][0], mid_point[0][1])
    value += manhaton(mid_point[-1][0], mid_point[-1][1], ex, ey)
    if m != 1:
        for j in range(1, m):
            value += manhaton(mid_point[j-1][0], mid_point[j-1][1], mid_point[j][0], mid_point[j][1]) 

    answer.append(value)

print(answer.index(min(answer))+1)