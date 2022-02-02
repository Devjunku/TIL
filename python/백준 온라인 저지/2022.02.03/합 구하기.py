import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

for i in range(1, n+1):
    arr[i] += arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j]-arr[i-1])