def solution(n, k, cmd):

    exist = [True for _ in range(n)]
    max_n = n-1
    min_n = 0
    stack = []

    for c in cmd:
        signal = c[0]
        if signal == 'U':
            i = int(c[2])
            while i:
                if exist[k]:
                    k -= 1
                    i -= 1
                else:
                    continue
        
        elif signal == 'D':
            i = int(c[2])
            while i:
                if exist[k]:
                    k += 1
                    i -= 1
                else:
                    continue

        elif signal == 'C':
            exist[k] = False
            stack.append(k)
            if k == max_n:
                
                


    pass

if __name__ == '__main__':
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))