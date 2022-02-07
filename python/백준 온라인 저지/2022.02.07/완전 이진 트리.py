import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
k = int(input())
arr = list(map(int, input().split()))
res = [[] for _ in range(1, k+1)]

def binary_separation(arr, depth):
    if len(arr) == 1:
        res[depth].extend(arr)
        return
    
    length = len(arr)
    mid = length // 2
    res[depth].append(arr[mid])
    binary_separation(arr[:mid], depth+1)
    binary_separation(arr[mid+1:], depth+1)
    
binary_separation(arr, 0)


for i in range(k):
    if i == 0:
        print(res[i][0])
    else:
        print(*res[i])