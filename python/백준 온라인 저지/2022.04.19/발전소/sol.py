import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
turn_on_cost = []

for _ in range(n):
    turn_on_cost.append(list(map(int, input().split())))

cur_state = input().strip()
turn_on_min = int(input())
dp = [1000] * (1 << n)

time, now = 0, 0
for i in range(len(cur_state)):
    if cur_state[-i-1] == "Y":
        now += 2 ** i
        time += 1

q = deque()
def solution():
    global now, time, n, q

    dp[now] = 0
    answer = 1000

    if turn_on_min == 0 or time >= turn_on_min:
        return 0

    elif time == 0:
        return -1
    
    else:
        q.append((now, 0))

    
    while time < turn_on_min:
        size = len(q)
        for _ in range(size):
            now, cost = q.popleft()
            for i in range(n):

                if (1 << i) & now == 0:
                    tmp = sys.maxsize
                    for j in range(n):
                        if (1 << j) & now == 1 << j:
                            tmp = min(tmp, turn_on_cost[n-1-j][n-1-i])
                    
                    if dp[now + (1 << i)] > cost + tmp:
                        q.append((now+ (1 << i), cost+tmp))
                        dp[now + (1 << i)] = cost+tmp
        
        time += 1

    while q:
        _, cost = q.pop()
        answer = min(answer, cost)

    return answer

print(solution())

