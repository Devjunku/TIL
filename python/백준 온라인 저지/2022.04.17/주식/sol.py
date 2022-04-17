import sys
input = sys.stdin.readline

def bs(left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if dp[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    price = list(map(int, input().split()))

    dp = [price[0]]

    for i in range(1, n):
        if dp[-1] < price[i]:
            dp.append(price[i])
        else:
            idx = bs(0, len(dp)-1, price[i])
            dp[idx] = price[i]

    print(f"Case #{t}")
    print(1) if len(dp) >= k else print(0)
