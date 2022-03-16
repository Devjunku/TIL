import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] + [int(input()) for _ in range(n)]

for i in range(1, n+1):
    arr[i] += arr[i-1]
    
for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        new_num = c - (arr[b] - arr[b-1])
        for i in range(b, n+1):
            arr[i] += new_num
    else:
        print(arr[c] - arr[b-1])