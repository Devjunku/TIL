import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def my_MaxValueIndex(x):
    idx = 0
    dat = x[0]
    for i in range(1, len(x)):
        if x[i] > dat:
            dat = x[i]

    for i in range(1, len(x)):
        if x[i] == dat:
            idx = i
    return [idx, dat]

for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, list(input())))
    num_list = [0] * 10
    for i in range(len(numbers)):
        num_list[numbers[i]] += 1
    res = my_MaxValueIndex(num_list)
    print('#{} {} {}'.format(t, res[0], res[1]))



    #########################################



