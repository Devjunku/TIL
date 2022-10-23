import sys
input = sys.stdin.readline

d, n = map(int, input().split())


oven_depth = list(map(int, input().split()))
pizza = list(map(int, input().split()))
toggle = [False for _ in range(d)]

if n > d: print(0); exit();

mini = int(100000)
min_depth = [int(100000) for _ in range(d)]


for i in range(d):
    mini = min(mini, oven_depth[i])
    min_depth[i] = mini

min_depth.reverse()
answer = 0
oven_idx = 0
pizza_idx = 0
while oven_idx < d and pizza_idx < n:

    if min_depth[oven_idx] >= pizza[pizza_idx]:
        toggle[oven_idx] = True
        oven_idx += 1
        pizza_idx += 1
    elif min_depth[oven_idx] < pizza[pizza_idx]:
        oven_idx += 1

answer = 0
num = 0
for i in range(d):
    if toggle[i]:
        answer = d - i
        num += 1

print(answer) if num == n else print(0)