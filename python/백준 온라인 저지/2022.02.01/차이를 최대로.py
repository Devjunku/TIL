import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

def permutation(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, ele in enumerate(arr):
        for P in permutation(arr[:i]+arr[i+1:], n-1):
            result += [[ele] + P]
    
    return result
    
answer = 0

for permu in permutation(arr, n):
    res = 0
    for i in range(n-1):
        res += abs(permu[i]-permu[i+1])
    
    if res > answer:
        answer = res

print(answer)