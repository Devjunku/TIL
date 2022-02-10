import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    arr[i] += arr[i-1]


maxv = 0
for i in range(m, n+1):
    if maxv < arr[i] - arr[i-m]:
        maxv = arr[i] - arr[i-m]

print(maxv)