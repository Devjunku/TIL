import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    iron = input()
    ans = ''
    i = 0
    stacks = []
    while i < len(iron):
        if iron[i:i+2] == '()':
            ans += 'l'
            i += 2
        elif iron[i] == '(':
            ans += iron[i]
            i += 1
        elif iron[i] == ')':
            ans += iron[i]
            i += 1
        elif i == len(iron)-1:
            ans += iron[i]
            i += 1
    print(ans)

    for i in range(len(ans)):
        if ans[i] == '(':
            stacks.append(i)

    print(stacks)

    res_cnt = 0
    for stack in stacks:
        k = stack
        bound = 0
        stack_list = [stack]
        while True:
            if ans[k] == '(':
                bound += 1
            elif ans[k] == ')':
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
            if ans[k1] == 'l':
                cnt1 += 1
            k1 += 1
        res_cnt += cnt1

    print('#{} {}'.format(t, res_cnt))