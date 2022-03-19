from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
color_ball = []
dic = defaultdict(int)
for i in range(n):
    c, s = map(int, input().split())
    color_ball.append((c, s, i))

color_ball.sort(key=lambda x : (x[1], x[0]))

answer = defaultdict(int)
ball_size_sum = defaultdict(int)

total = 0
j = 0
for i in range(n):
    while color_ball[j][1] < color_ball[i][1]:
        total += color_ball[j][1]
        ball_size_sum[color_ball[j][0]] += color_ball[j][1]
        j += 1
    answer[color_ball[i][2]] = total - ball_size_sum[color_ball[i][0]]

for i in range(n):
    print(answer[i])


1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8