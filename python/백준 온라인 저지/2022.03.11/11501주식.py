import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stock_price = list(map(int, input().split()))

    result = 0

    mx_v = stock_price[-1]

    for i in range(n-2, -1, -1):
        if stock_price[i] > mx_v:
            mx_v = stock_price[i]
        else:
            result += (mx_v - stock_price[i])

    print(result)