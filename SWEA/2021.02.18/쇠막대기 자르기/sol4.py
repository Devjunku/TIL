import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    string = input()
    l = []
    layer_list = []
    i = 0
    while i < len(string):
        if string[i:i+2] == '()':
            l.append([i, i+1])
            i += 2
        elif string[i] == '(':
            k = i
            stack = 0
            stack_list = [k]
            while k < len(string):
               if string[k] == '(':
                   stack += 1
               else:
                   stack -= 1
               if stack == 0:
                   stack_list.append(k)
                   layer_list.append(stack_list)
                   break
               k += 1
            i += 1
        else:
            i += 1

    res_cnt = 0
    for bound in layer_list:
        cnt = 1
        for laser in l:
            if bound[0] < laser[0] and laser[1] < bound[1]:
                cnt += 1
        if cnt != 1:
            res_cnt += cnt

    print('#{} {}'.format(t, res_cnt))

