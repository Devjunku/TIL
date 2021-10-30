def solution(n, k, cmd):

    exist = [True for _ in range(n)]
    up = [-1] + [x for x in range(n-1)]
    down = [x for x in range(1, n)] + [-1]
    deleted = []


    for c in cmd:
        op = c[0]

        if op == 'U':
            val = int(c.split()[1])
            for _ in range(val):
                k = up[k] # k는 계속 현재의 위치
        
        elif op == 'D':
            val = int(c.split()[1])
            for _ in range(val):
                k = down[k]
            
        elif op == 'C':
            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != -1:
                up[down[k]] = up[k]
            exist[k] = False
            deleted.append(k)

            k = down[k] if down[k] != -1 else up[k]

        elif op == 'Z':
            d = deleted.pop()
            if up[d] != -1:
                down[up[d]] = d
            if down[d] != -1:
                up[down[d]] = d
            
            exist[d] = True
    
        else:
            raise RuntimeError(op)

    return "".join('O' if x else 'X' for x in exist) 

if __name__ == '__main__':
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))