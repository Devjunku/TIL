import sys
from copy import deepcopy
input = sys.stdin.readline

test_case = int(input().strip())

answer = 0
for t in range(test_case):
    string1 = input().strip()
    string2 = deepcopy(string1)
    number = 0
    while "for" in string1:
        start_idx = string1.find("for")
        string1 = string1.replace(string1[:start_idx+3], "", 1)
        number += 1
    
    while "while" in string2:
        start_idx = string2.find("while")
        string2 = string2.replace(string2[:start_idx+5], "", 1)
        number += 1
    answer = max(answer, number)

print(answer)