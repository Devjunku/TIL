import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    test_case = list(map(int, input().split()))

    if len(test_case) == 1:
        break

    k = test_case[0]
    lotto_list = test_case[1:]

    for lotto_number in combinations(lotto_list, 6):
        print(*lotto_number)
    
    print()