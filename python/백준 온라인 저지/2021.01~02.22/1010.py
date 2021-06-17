# t = int(input())

# N, M = map(int, input().split())


# N, M = 13, 29

cnt = 1
for i in range(M, M-N, -1):
    cnt *= i

cnt1 = 1
for i in range(N, 0, -1):
    cnt1 *= i


print(int(cnt/cnt1))

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    cnt = 1
    for i in range(M, M-N, -1):
        cnt *= i
    cnt1 = 1
    for i in range(N, 0, -1):
        cnt1 *= i
    print(int(cnt/cnt1))