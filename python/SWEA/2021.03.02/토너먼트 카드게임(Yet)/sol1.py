import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    card_num = list(map(int, input().split()))
    stack_1 = []
    idx_1 = []
    for i in range(0, N, 2):
        stack_2 = []
        stack_3 = []
        for j in range(2):
            if i+j < N:
                stack_2.append(card_num[i+j])
                stack_3.append(i+j)
            else:
                break
        stack_1.append(stack_2)
        idx_1.append(stack_3)
    # print(stack_1)
    # print(idx_1)
    stack_2 = []
    idx_2 = []
    while True:
        stack_2 = []
        idx_2 = []
        for i in range(len(stack_1)):
            if len(stack_1[i]) == 2:
                if stack_1[i][0] == 1 and stack_1[i][1] == 2:
                    stack_2.append(stack_1[i][1])
                    idx_2.append(idx_1[i][1])
                elif stack_1[i][0] == 2 and stack_1[i][1] == 1:
                    stack_2.append(stack_1[i][0])
                    idx_2.append(idx_1[i][0])
                elif stack_1[i][0] == 2 and stack_1[i][1] == 3:
                    stack_2.append(stack_1[i][1])
                    idx_2.append(idx_1[i][1])
                elif stack_1[i][0] == 3 and stack_1[i][1] == 2:
                    stack_2.append(stack_1[i][0])
                    idx_2.append(idx_1[i][0])
                elif stack_1[i][0] == 1 and stack_1[i][1] == 3:
                    stack_2.append(stack_1[i][0])
                    idx_2.append(idx_1[i][0])
                elif stack_1[i][0] == 3 and stack_1[i][1] == 1:
                    stack_2.append(stack_1[i][1])
                    idx_2.append(idx_1[i][1])
                elif stack_1[i][0] == stack_1[i][1]:
                    if idx_1[i][0] < idx_1[i][1]:
                        stack_2.append(stack_1[i][0])
                        idx_2.append(idx_1[i][0])
                    else:
                        stack_2.append(stack_1[i][1])
                        idx_2.append(idx_1[i][1])
            else:
                stack_2.extend(stack_1[i])
                idx_2.extend(idx_1[i])
        # print('stack_2', stack_2)
        # print('idx_2', idx_2)
        stack_1 = []
        idx_1 = []
        for i in range(0, len(stack_2), 2):
            stack_3 = []
            idx_3 = []
            for j in range(2):
                if i + j < len(stack_2):
                    stack_3.append(stack_2[i + j])
                    idx_3.append(idx_2[i + j])
                else:
                    break
            stack_1.append(stack_3)
            idx_1.append(idx_3)

        # print('stack_1', stack_1)
        # print('idx_1', idx_1)

        if len(stack_1) == 1:
            stack_2 = []
            idx_2 = []
            if stack_1[0][0] == 1 and stack_1[0][1] == 2:
                stack_2.append(stack_1[0][1])
                idx_2.append(idx_1[0][1])
            elif stack_1[0][0] == 2 and stack_1[0][1] == 1:
                stack_2.append(stack_1[0][0])
                idx_2.append(idx_1[0][0])
            elif stack_1[0][0] == 2 and stack_1[0][1] == 3:
                stack_2.append(stack_1[0][1])
                idx_2.append(idx_1[0][1])
            elif stack_1[0][0] == 3 and stack_1[0][1] == 2:
                stack_2.append(stack_1[0][0])
                idx_2.append(idx_1[0][0])
            elif stack_1[0][0] == 1 and stack_1[0][1] == 3:
                stack_2.append(stack_1[0][0])
                idx_2.append(idx_1[0][0])
            elif stack_1[0][0] == 3 and stack_1[0][1] == 1:
                stack_2.append(stack_1[0][1])
                idx_2.append(idx_1[0][1])
            elif stack_1[0][0] == stack_1[0][1]:
                if idx_1[0][0] < idx_1[0][1]:
                    stack_2.append(stack_1[0][0])
                    idx_2.append(idx_1[0][0])
                else:
                    stack_2.append(stack_1[0][1])
                    idx_2.append(idx_1[0][1])
            break

    print('#{} {}'.format(t, idx_2[0]+1))

