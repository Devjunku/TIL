def elementNum(N):

    cnt = 1
    for i in range(1, N // 2 + 1):
        if not N % i:
            
            cnt += 1
    return cnt

def solution(left, right):
    
    answer = 0
    for i in range(left, right+1):

        if not elementNum(i) % 2:
            answer += i
        else:
            answer -= i


    return answer

if '__main__' == __name__:
    print(solution(13, 17))
    print(solution(24, 27))
    print(solution(1, 1))