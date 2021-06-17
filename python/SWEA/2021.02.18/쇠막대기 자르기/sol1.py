import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    iron = input()
    ans = []
    i = 0
    while i < len(iron):
        if iron[i:i+2] == '()':
            ans.append('l')
            i += 2
        elif iron[i] == '(':
            ans.append('(')
            i += 1
        elif iron[i] == ')':
            ans.append(')')
            i += 1
        elif i == len(iron)-1:
            ans.append(')')
            i += 1

    N_list = []
    stack = 0
    layer = 0
    for j in range(len(ans)):
        if ans[j] == 'l':
            N_list.append('l')
            continue
        elif ans[j] == '(':
            layer += 1
            N_list.append(layer)
            if stack < layer:
                stack += 1
        elif ans[j] == ')':
            layer -= 1
            N_list.append(layer + 1)

    arr = []
    for k in range(len(N_list)-1):
        arr.append(N_list[k])
        if type(N_list[k]) == int and type(N_list[k+1]) == int and N_list[k] == N_list[k+1]:
            arr.append(N_list[k]-0.5)

        if k == len(N_list)-2:
            arr.append(N_list[k+1])

    res_cnt = 0
    for i in range(1, stack+1):
        j = 0
        stack_list = []
        while j < len(arr):
            if arr[j] == i:
                stack_list.append(j)
            if len(stack_list) == 2:
                k1 = stack_list[0]
                k2 = stack_list[1]
                stack_list = []
                cnt = 1
                while k1 <= k2:
                    if arr[k1] == 'l':
                        cnt += 1
                    k1 += 1
                res_cnt += cnt
            j += 1

    print('#{} {}'.format(t,res_cnt))






