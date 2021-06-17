import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    work = input()
    iron = 0
    result = 0

    for i in range(len(work)):
        if work[i] == '(':
            iron += 1
        else:
            iron -= 1
            if work[i - 1] == '(':
                result += iron
            else:
                result += 1



    print('#{} {}'.format(tc, result))