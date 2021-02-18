import sys

sys.stdin = open('1_input.txt')

# 2021.02.16 소수 뭉치를 만들까 생각함.
prime_list = [2]

# 소수 판별
def prime(n):
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# n 다음의 소수 찾기
def nextprime(n):
    num = n + 1
    while True:
        if prime(num):
            break
        else:
            num += 1
    return num

# 소인수 분해
def factorization(n):
    if n == 1:
        return [[1], [1]]
    number = n
    k = 2
    factor_idx = []
    power_num = []
    while True:
        a = 0
        while True:
            if number % k == 0:
                a += 1
                number //= k
            else:
                break

        if a != 0:
            factor_idx.append(k)
            power_num.append(a)
            total = 1
            for i in range(len(factor_idx)):
                total *= factor_idx[i]**power_num[i]
            if total == n:
                break
        k = nextprime(k)
    return [factor_idx,power_num]

# 본 문제 풀이
T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 소인수분해 리스트 저장
    arr = factorization(N)

    # N값이 1이면 그냥 출력
    if N == 1:
        print('#{} {}'.format(t, 1))
    #그렇지 않고 소수면 소수를 출력
    elif prime(N):
        print('#{} {}'.format(t, N))
    # 그렇지 않으면
    else:
        num = 1
        i = 0
        while i < len(arr[1]): # 리스트안의 원소의 원소 개수 만큼 돌면서
            if arr[1][i] % 2 == 1: # 홀수인 부분의 소인수를 num에 곱하기
                num *= arr[0][i]
                i += 1 # 그리고 idx 1추가
            else: # 그렇지 않아도 1추가
                i += 1
        print('#{} {}'.format(t, num)) # 출력












