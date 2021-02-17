def solution(a, b):
    month = [0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    total_day = sum(month[0:a]) + b
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return day[(total_day%7)-1]

if __name__ == '__main__':
    print(solution(5, 24))