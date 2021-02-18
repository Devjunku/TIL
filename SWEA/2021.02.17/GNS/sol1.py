import sys

sys.stdin = open('GNS_test_input.txt')

num_string = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for t in range(1, T+1):
    I, N = map(str, input().split())
    test_list = list(map(str, input().split()))

    num_list = [0] * 10
    for i in range(len(test_list)):
        if test_list[i] == "ZRO":
            num_list[0] += 1
        elif test_list[i] == "ONE":
            num_list[1] += 1
        elif test_list[i] == "TWO":
            num_list[2] += 1
        elif test_list[i] == "THR":
            num_list[3] += 1
        elif test_list[i] == "FOR":
            num_list[4] += 1
        elif test_list[i] == "FIV":
            num_list[5] += 1
        elif test_list[i] == "SIX":
            num_list[6] += 1
        elif test_list[i] == "SVN":
            num_list[7] += 1
        elif test_list[i] == "EGT":
            num_list[8] += 1
        elif test_list[i] == "NIN":
            num_list[9] += 1

    res_str = ''
    for i in range(len(num_string)):
        res_str += (num_string[i] + ' ') * num_list[i]

    print(I)
    print(res_str[0:len(res_str) - 1])


