def solution(n):
    
    ans_list = [[0]*i for i in range(1, n+1)]
    
        # res = []
        # for i in range(1, n+1):
        #     res.append(i)

    r = -1
    c = 0
    direction = 1
    i = 1
    while True:

        if n == 0:
            break

        for j in range(n):
            r += direction
            ans_list[r][c] = i
            i += 1
        
        n -= 1

        if n == 0:
            break

        for j in range(n):
            c += direction
            ans_list[r][c] = i
            i += 1

        n -= 1

        if n == 0:
            break

        direction *= -1
        for j in range(n):
            r += direction
            c += direction
            ans_list[r][c] = i
            i += 1

        n -= 1

        if n == 0:
            break

        direction *= -1
    
    answer = []
    for e in ans_list:
        answer.extend(e)

    return answer

if __name__ == '__main__':
    print(solution(4))
    print(solution(5))
    print(solution(6))