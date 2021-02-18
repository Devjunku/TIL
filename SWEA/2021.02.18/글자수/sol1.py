import sys

sys.stdin = open('sample_input.txt')


def my_func(N_list):
    dat = N_list[0]
    for i in range(1, len(N_list)):
        if dat < N_list[i]:
            dat = N_list[i]
    return dat


T = int(input())

for t in range(1, T+1):

    str1 = input()
    str2 = input()

    zero_list = [0] * len(str1)
    for s1 in range(len(str1)):
        for s2 in str2:
            if str1[s1] == s2:
                zero_list[s1] += 1

    print('#{} {}'.format(t, my_func(zero_list)))

