

def prime_num(nums):
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True
        
from itertools import combinations

def solution(nums):
    res = 0
    res_samples = list(combinations(nums, 3))
    print(res_samples)
    for res_sample in res_samples:
        print(sum(res_sample))
        if prime_num(sum(res_sample)):
            res += 1

    return res

print(solution([1,2,7,6,4]))