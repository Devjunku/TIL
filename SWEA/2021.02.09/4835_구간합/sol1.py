import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def my_sum(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total

for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    min_value = my_sum(numbers[0:M])
    max_value = my_sum(numbers[0:M])
    for i in range(1, N-M+1):
        if my_sum(numbers[i:i+M]) < min_value:
            min_value = my_sum(numbers[i:i+M])
        if my_sum(numbers[i:i+M]) > max_value:
            max_value = my_sum(numbers[i:i + M])
    print('#{} {}'.format(t, max_value - min_value))


