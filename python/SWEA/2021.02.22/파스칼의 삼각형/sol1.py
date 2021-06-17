import sys

sys.stdin = open('input.txt')

T = int(input())

def combination(N, R):
    n = 1
    for i in range(N, N-R, -1):
        n *= i
    r = 1
    for i in range(1, R+1):
        r *= i
    
    return int(n / r)

# print(combination(5, 3))

def solution(N):
    arr = []
    for i in range(N+1):
        arr.append(combination(N, i))

    return arr


for t in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(0, N):
        arr.append(solution(n))
    
    print('#{}'.format(t))
    for n in range(len(arr)):
        print(*arr[n])
