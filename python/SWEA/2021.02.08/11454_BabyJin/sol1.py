import sys

sys.stdin = open('input.txt')

T = int(input())
print(T)
for tc in range(1, T+1):
    numbers = list(map(int, list(input())))
    counter = [0] * len(numbers)
    is_babyjin = 0
    for i in range(len(numbers)):
        counter[i] += 1
        print(counter)
    for idx in range(len(counter)):
        # tri 검증
        if counter[idx] >= 3:
            is_babyjin += 1
            counter[idx] -= 3
        # run 검증
        if idx < 8:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babyjin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
    if is_babyjin == 2:
        print('#{0} {1}'.format(tc, 1))
    else:
        print('#{0} {2}'.format(tc, 0))







