import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

arr = [0 for _ in range(100000*20)]

for i in range(1 << 20):
    tmp = 0
    for j in range(n):
        if i & (1 << j):
            tmp += a[j]
    arr[tmp] = 1

for i in range(1 << 20):
    if arr[i] != 1:
        print(i)
        break