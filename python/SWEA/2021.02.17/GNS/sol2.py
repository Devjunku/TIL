T = int(input())
num_string = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for t in range(1, T+1):
    num_list = [0] * 10
    I, N = map(str, input().split())
    test_list = input().split()

    for num in test_list:
        idx = num_string.index(num)
        num_list[idx] += 1

    res_str= []
    for i in range(10):
        res_str += [num_string[i]] * num_list[i]

    res_str = ' '.join(res_str)
    print(I)
    print(res_str)