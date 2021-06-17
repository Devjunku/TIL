from itertools import permutations

def prime(num_case):
    prime_list = []
    for n in num_case:
        cnt = 0
        for i in range(2, n):
            if n % i == 0:
                cnt += 1
                break
        if n > 1 and cnt == 0:
            prime_list.append(n)
    return len(prime_list)

def solution(numbers):
    num_case = []
    for i in range(1, len(numbers)+1):
        tmp  = permutations(numbers, i)
        for n in tmp:
            tmp_str = ''.join(n)
            num_case.append(int(tmp_str))
    num_case=list(set(num_case))
    return prime(num_case)