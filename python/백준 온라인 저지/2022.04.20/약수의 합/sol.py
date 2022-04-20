import sys
input = sys.stdin.readline

M = 1000000

dp = [1] * (M+1)
cumsum = [0] * (M+1)

for i in range(2, M+1):
    j = 1
    while i*j <= M:
        dp[i*j] += i
        j += 1
    

for i in range(1, M+1):
    cumsum[i] = cumsum[i-1] + dp[i]

t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    answer.append(f"{cumsum[n]}")

print("\n".join(answer))