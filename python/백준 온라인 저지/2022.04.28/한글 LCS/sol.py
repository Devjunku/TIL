import sys
input = sys.stdin.readline

s1, s2 = input().strip(), input().strip()
n1 = len(s1)
n2 = len(s2)
dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

answer = 0
for i in range(n1):
    for j in range(n2):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j]+1
            answer = max(answer, dp[i+1][j+1])
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            answer = max(answer, dp[i+1][j+1])

print(answer)