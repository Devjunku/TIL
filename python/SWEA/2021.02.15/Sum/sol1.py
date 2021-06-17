import sys

sys.stdin = open('input.txt')

def max_func(ex_list):
    max_ele = ex_list[0]
    for i in range(1, len(ex_list)):
        if max_ele < ex_list[i]:
            max_ele = ex_list[i]
    return max_ele


for t in range(1, 11):
    case = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []
    sum_value3 = 0
    for i in range(len(arr)):
        sum_value1 = 0
        sum_value2 = 0
        sum_value3 += arr[i][i]

        for j in range(len(arr[i])):
            sum_value1 += arr[i][j]
            sum_value2 += arr[j][i]

        sum_list.append(sum_value1)
        sum_list.append(sum_value2)

    sum_list.append(sum_value3)
    ans = max_func(sum_list)

    print('#{} {}'.format(t, ans))




