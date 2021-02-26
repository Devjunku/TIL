

def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n // 2):
            if n % i == 0:
                return False
    return True
            



def solution(nums):
    cnt = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                if prime(sum([nums[i], nums[j], nums[k]])):
                    cnt += 1
    return cnt




if __name__ == '__main__':
    print(solution([1,2,3,4]))
    print(solution([1,2,7,6,4]))