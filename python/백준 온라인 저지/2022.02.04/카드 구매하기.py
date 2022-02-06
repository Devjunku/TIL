import sys
input = sys.stdin.readline

n = int(input())
plist = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + plist[j])
        print(dp)
    
print(dp[n])