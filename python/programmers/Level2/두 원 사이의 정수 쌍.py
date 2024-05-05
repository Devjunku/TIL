import math

def num_point(number):
    
    (number * 2 + 1) ** 2
    
    # number * 2 + 1
    
    start = 0
    end = number
    
    while start < end:
        m = (start + end) // 2
        print(math.sqrt(2) * m, m)
        if math.sqrt(2) * m < number:
            start = m + 1
        else:
            end = m
    
        # print(start, end)

    return m


def solution(r1, r2):
    
    print(num_point(r2))
    
    return

if __name__ == "__main__":
    print(solution(2, 6))