import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 입력 숫자를 리스트로 바꾼다
    numbers = list(map(int, input().split()))
    # 리스트의 총 합을 구한다
    total = 0
    for idx in range(len(numbers)):
        total += numbers[idx]
    avg = round(total / len(numbers))
    print('#{} {}'.format(tc, avg))
