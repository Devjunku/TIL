import sys
n = int(input())
distance = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

cost.pop()

more_small = 1000000001
answer = 0

for d, c in zip(distance, cost):
    if more_small > c:
        more_small = c
        answer += (more_small*d)
    else: answer += (more_small*d)

print(answer)

# print(distance)
# print(cost)