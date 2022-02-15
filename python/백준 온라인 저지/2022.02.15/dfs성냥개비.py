# backtracking 풀이 틀림...

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

matches_key = ["1", "7", "4", "2", "3", "5", "6", "9", "0", "8"]
matches_value = [2, 3, 4, 5, 5, 5, 6, 6, 6, 7]

def dfs(num, string):
    global minimum, maximum

    if num == 0:
        if string[0] == "0":
            return
        minimum = min(minimum, int(string))
        maximum = max(maximum, int(string))
        return

    if num < 0:
        return

    for i in range(0, 10):
        if num - matches_value[i] >= 0:
            dfs(num-matches_value[i], string+str(matches_key[i]))

testcase_number = int(input())

for testcase in range(testcase_number):
    minimum = int(1e9)
    maximum = 0
    number = int(input())
    dfs(number, "")
    print(f"{minimum} {maximum}")