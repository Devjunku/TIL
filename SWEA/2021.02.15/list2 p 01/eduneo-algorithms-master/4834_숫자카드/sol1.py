# 문제풀이 계속 진행

# 현재 문제 푸는게 너무 어려운 분은 저에게 DM

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    # 카운트할 리스트 만들기
    counts = [0] * 10
    for number in numbers:
        counts[number] += 1

    print(counts)

    # max count 구하기
    highest_idx = 0
    for idx in range(len(counts)):
        if counts[idx] >= counts[highest_idx]:
            highest_idx = idx
    print(highest_idx, counts[highest_idx])
