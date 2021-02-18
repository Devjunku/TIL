import sys

sys.stdin = open('input.txt')

T = int(input())
alphabets = [2, 3, 5, 7, 11]
for t in range(1, T+1):
    nums = ''
    N = int(input())
    for i in range(len(alphabets)):
        cnt = 0
        while True:
            if N % alphabets[i] == 0:
                cnt += 1
                N = N // alphabets[i]
            else:
                break
        nums += str(cnt) + ' '
    print('#{} {}'.format(t, nums[0:len(nums)-1]))

