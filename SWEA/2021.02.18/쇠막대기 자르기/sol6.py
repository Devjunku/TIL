import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    string = input().replace('()', 'l')
    res_cnt = 0
    stacks = []

    for i in range(len(string)):
        if string[i] == '(':
            stacks.append(i)

    res_cnt = 0
    for stack in stacks:
        k = stack
        bound = 0
        stack_list = [stack]
        while True:
            if string[k] == '(':
                bound += 1
            elif string[k] == ')':
                bound -= 1
                if bound == 0:
                    stack_list.append(k)
                    break
            k += 1
        # print(stack_list)
        k1 = stack_list[0]
        k2 = stack_list[1]
        cnt1 = 1
        while k1 <= k2:
            if string[k1] == 'l':
                cnt1 += 1
            k1 += 1
        res_cnt += cnt1

    print('#{} {}'.format(t, res_cnt))







