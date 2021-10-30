import sys

cnt = sys.maxsize



def select(t, s):
    global cnt, time, nums

    if cnt < s:
        return

    if t < 0:
        return

    if t == 0:
        if s < cnt:
            cnt = s
        return

    for



def solution():
    time = [300, 130, 120, 20]
    nums = [10, 30, 20, 30]

if __name__ == '__main__':
    print(solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]))