from copy import deepcopy
N =  int(input())

dp = [0 for _ in range(1000)]
dp[0] = 10

d1 = [1 for _ in range(10)]
d2 = [i for i in range(10, 0, -1)]
for i in range(1, 1000):
    d2[0] = dp[i-1]
    for j in range(1, 10):
        d2[j] = d2[j-1] - d1[j-1]
    d1 = deepcopy(d2)
    dp[i] = sum(d2)

print(dp[N-1] % 10007)