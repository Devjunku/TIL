import sys
sys.stdin = open('input.txt')

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    # pivot을 기준으로 pivot보다 작은 숫자들은 left에, 큰 숫자는 right에 모은다
    left, right = [], []
    pivot = nums[0]

    for idx in range(1, len(nums)):
        if nums[idx] < pivot:
            left.append(nums[idx])
        elif nums[idx] > pivot:
            right.append(nums[idx])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return [*sorted_left, pivot, *sorted_right]

T = int(input())

for t in range(1, T+1):
    N = len(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(t, quick_sort(numbers)))