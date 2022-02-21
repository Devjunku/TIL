import sys
input = sys.stdin.readline

n = int(input())

isBonus = {
    i: False for i in range(1, n+1)
}

korea_list = []
english_list = []
math_list = []
science_list = []

for i in range(1, n+1):
    number, korea, english, math, science = map(int, input().split())
    korea_list.append((number, korea))
    english_list.append((number, english))
    math_list.append((number, math))
    science_list.append((number, science))

korea_list.sort(key=lambda x: (x[1], -x[0]))
english_list.sort(key=lambda x: (x[1], -x[0]))
math_list.sort(key=lambda x: (x[1], -x[0]))
science_list.sort(key=lambda x: (x[1], -x[0]))

def find_first_number(score_list):
    for i in range(n-1, -1, -1):
        first, score = score_list[i]
        if not isBonus[first]:
            isBonus[first] = True
            return first

answer = []
for score_list in [korea_list, english_list, math_list, science_list]:
    answer.append(find_first_number(score_list))

print(*answer)