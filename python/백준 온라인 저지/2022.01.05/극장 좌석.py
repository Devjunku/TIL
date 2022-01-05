n = int(input())
m = int(input())

if n >= 2:
    dp = [1 for _ in range(n+1)]
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    i = 1
    answer = []
    for _ in range(m):
        idx = int(input())
        answer.append(idx-i)
        i = idx+1
    answer.append(n-i+1)

    res = 1
    for a in answer:
        res *= dp[a]
    print(res)
else:
    for _ in range(m):
        v = int(input())
    print(1)
