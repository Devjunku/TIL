import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
t = int(input())

dp = [-1] * 2501
MOD = 1000000007
def make_dp(n):
    if n == 0:
        return 1
    elif dp[n] != -1:
        return dp[n]
    
    result = 0
    for i in range(n):
        result += (make_dp(i) * make_dp(n-i-1)) % MOD
        result %= MOD
    
    dp[n] = result
    return result

for _ in range(t):
    a = int(input())
    if a % 2 == 1:
        print(0)
    else:
        print(make_dp(a//2))