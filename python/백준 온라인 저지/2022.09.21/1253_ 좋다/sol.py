import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

num = 0

for i in range(n):
    sub_list = numbers[:i] + numbers[i+1:]
    start, end = 0, len(sub_list) - 1

    while start < end:

        mid = sub_list[start] + sub_list[end]

        if numbers[i] == mid:
            num += 1
            break
        elif numbers[i] > mid:
            start += 1
        else:
            end -= 1

print(num)