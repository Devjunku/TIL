from sys import stdin

N = int(stdin.readline().rstrip())

idx = []
value = []
for i in range(N):
    ie, ve = map(int, stdin.readline().rstrip().split())
    idx.append(ie-1)
    value.append(ve)
arr = [0] * (max(idx)+1)
for i, v in zip(idx, value):
    arr[i] = v

midx = arr.index(max(arr))
for i in range(midx):
    if arr[i+1] < arr[i]:
        arr[i+1] = arr[i]
for i in range(len(arr)-1, midx, -1):
    if arr[i] > arr[i-1]:
        arr[i-1] = arr[i]
print(sum(arr))
