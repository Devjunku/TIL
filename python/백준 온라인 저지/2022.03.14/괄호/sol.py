# from collections import defaultdict
# def dfs(left, right, string):
#     if left < 0 or right < 0:
#         return
        
#     if left == 0 and right == 0:
#         dic[string]
#         return
    
#     dfs(left-1, right, string+"(")
#     if right > left:
#         dfs(left, right-1, string+")")

import sys
input = sys.stdin.readline
t = int(input())

dp = [0] * 5001
dp[0] = 1

for i in range(2, 5001, 2):
    for j in range(2, i+1, 2):
        dp[i] += (dp[j-2] * dp[i-j]) % 1000000007

for _ in range(t):
    l = int(input())
    print(dp[l] % 1000000007)