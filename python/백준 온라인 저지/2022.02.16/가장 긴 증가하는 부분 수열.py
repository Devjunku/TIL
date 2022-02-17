import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(0, n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i]+1, dp[j])

print(max(dp))