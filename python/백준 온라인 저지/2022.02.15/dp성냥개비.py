import sys
input = sys.stdin.readline

testcase_number = int(input())

matches_key = ["1", "7", "4", "2", "3", "5", "6", "9", "0", "8"]
matches_value = [2, 3, 4, 5, 5, 5, 6, 6, 6, 7]
dp = [[0, 0] for _ in range(100)]

for testcase in range(testcase_number):
    minimum = int(1e9)
    maximum = 0
    number = int(input())
    print(f"{minimum} {maximum}")