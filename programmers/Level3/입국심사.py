def solution(n, times):
    answer = 0
    
    length = len(times)
    left = 1
    right = (length+1) * max(times)
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        print(mid, cnt, answer, right, left)
        for time in times:
            cnt += mid // time
            
            if cnt >= n:
                break
        
        if cnt >= n:
            answer = mid
            right = mid - 1
        elif cnt < n:
            left = mid + 1

    
    return answer


if __name__ == '__main__':
    print(solution(6, [7, 10]))