from sys import stdin
N = int(stdin.readline().strip())

nums = []
for _ in range(N):
    nums.append(int(stdin.readline().strip()))
    Ms = ''
    for i in range(2, max(nums)//2):
        f_num = nums[0] % i
        cnt = 1
        for j in range(1, len(nums)):
            if nums[j] % i != f_num:
                break
            else:
                cnt += 1
        if cnt == len(nums):
            Ms += str(i)
if len(Ms) > 0:
    print(' '.join(Ms))


