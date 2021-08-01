from itertools import permutations
from copy import deepcopy

def operation(n1, n2, n3):
    if n2 == '*':
        return n1 * n3
    elif n2 == '+':
        return n1 + n3
    else:
        return n1 - n3


def firstOper(permu, nums):
    
    res = -int(1e9)
    for p in permu:
        num_copy = deepcopy(nums)
        for o in p:
            i = 0
            while i < len(num_copy):
                if num_copy[i] == o:
                    n1 = num_copy.pop(i-1)
                    n2 = num_copy.pop(i-1)
                    n3 = num_copy.pop(i-1)
                    num_copy.insert(i-1, operation(n1, n2, n3))
                i += 1
            if len(num_copy) > 2:
                num = operation(num_copy[0], num_copy[1], num_copy[2])
                absnum = abs(num)
                if absnum > res:
                    res = absnum
            else:
                absnum = abs(num_copy[0])
                if absnum > res:
                    res = absnum
    return res
                    
        
def solution(expression):
    
    nums = []
    opera = []
    num = []
    for i in expression:
        if i.isdigit():
            num.append(i)
        else:
            nums.append(int(''.join(num)))
            nums.append(i)
            opera.append(i)
            num = []
    
    nums.append(int(''.join(num)))    
    
    oper_set = list(set(opera))
    permu = permutations(oper_set, len(oper_set))
    res = firstOper(permu, nums)

    return res

if __name__ == "__main__":
    print(solution("100-200*300-500+20"))
    print(solution("50*6-3*2"))
    print(solution("3-50-6*5"))