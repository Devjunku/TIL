from pprint import pprint
import sys
input = sys.stdin.readline

n = int(input())
train = [0] + list(map(int, input().split()))
limit = int(input())

for i in range(1, n+1):
    train[i] += train[i-1]

total = train[-1]

dp = [[0]*(n+1) for _ in range(4)]

for i in range(1, 4):
    for j in range(limit*i, n+1):

        if n == 1:
            dp[i][j] = max(dp[i][j-1], train[j] - train[j-limit])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-limit] + train[j] - train[j-limit])

pprint(dp)
print(dp[3][n])