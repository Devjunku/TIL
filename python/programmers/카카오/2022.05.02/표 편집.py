def solution(n, k, cmd):

    exist_del = [True for _ in range(n)]
    up = [-1] + [i for i in range(n-1)]
    down = [i for i in range(1, n)] + [-1]
    stack = []

    for c in cmd:
        order = c[0]

        if order == "U":
            number = int(c.split()[1])
            for _ in range(number):
                k = up[k]

        elif order == "D":
            number = int(c.split()[1])
            for _ in range(number):
                k = down[k]
                
        elif order == "C":
            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != -1:
                up[down[k]] = up[k]
            exist_del[k] = False
            stack.append(k)

            k = down[k] if down[k] != -1 else up[k]

        elif order == "Z":
            dat = stack.pop()
            if up[dat] != -1:
                down[up[dat]] = dat
            if down[dat] != -1:
                up[down[dat]] = dat
            exist_del[dat] = True

    return "".join(["O" if exist else "X" for exist in exist_del])

    
  

if __name__ == "__main__":
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    # "OOOOXOOO"
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
    # "OOXOXOOO"
    