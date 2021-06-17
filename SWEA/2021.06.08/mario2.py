'''
<입력>
14
1 50 1 -1 1 3 -5 1 -15 0 100 1 1 2

<출력>
150
'''

def common_process(number):
    for i in range(2, number):
        numbers[i] += numbers[i-2]

# main
n = int(input())
numbers = list(map(int, input().split()))

if 3 <= n <= 7:
   common_process(n)

if 7 < n:
    common_process(7)

    for i in range(7, n):
        numbers[i] += max(numbers[i-2], numbers[i-7])

print(max(numbers))