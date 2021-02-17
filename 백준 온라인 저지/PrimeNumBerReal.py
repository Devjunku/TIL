def prime_num(nums):
    if nums == 1:
        return False
    elif nums == 2:
        return True
    else:
        for i in range(2, nums//2+1):
            if nums % i == 0:
                return False
        return True

n, m = map(int, input().split())

numbers = list(range(n , m+1))

cnt = 0
for number in numbers:
    if prime_num(number):
        cnt += 1
print(cnt)        




