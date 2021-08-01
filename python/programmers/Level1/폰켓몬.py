# 내풀이..
def solution(nums):
    N = int(len(nums)/2)
    
    nums.sort()
    pocket = {}
    keys = []
    for num in nums:
        if num in pocket.keys():
            pocket[num] += 1
        else:
            pocket[num] = 1
            keys.append(num)
    
    i = 0
    key_n = len(keys)
    answer = []
    while i < key_n:
        if keys[i] in answer or len(answer) >= N:
            break
        answer.append(keys[i])
        i += 1
        
    return len(answer)

# 다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))