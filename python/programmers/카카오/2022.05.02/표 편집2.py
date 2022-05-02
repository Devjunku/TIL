def solution(n, k, cmd):
    is_exist = [True for i in range(n)]
    up = [-1] + [i for i in range(n-1)]
    down = [i for i in range(1, n)] + [-1]
    stack = []

    now_idx = k

    for c in cmd:
        order = c[0]

        if order == "C":
            # 삭제할 때 맨 뒤의 인덱스 (더 이상 밑으로 내려갈 일이 없는 인덱스의 경우 )는 위로 올라가야 된다.
            # 그렇지 않은 경우에는 아래의 인덱스를 알려주어야 한다.
            # 예를 들어서
            # up이 -1 0 1 2 3
            # down이 1 2 3 4 -1
            # 인 경우에
            # now_idx의 값이 2(현재의 인덱스 값, up이 값이 -1이 아닌 경우)에서
            # C 연산을 수행한다고 하자.
            # 이때 삭제된 행에서 down[now_idx]값은 없어진 행 다음 값(now_idx+1, )이어야 한다.
            if up[now_idx] != -1:
                down[up[now_idx]] = down[now_idx]
            if down[now_idx] != -1:
                up[down[now_idx]] = up[now_idx]
            is_exist[k] = False
            stack.append(k)

            now_idx = down[now_idx] if down[now_idx] != -1 else up[now_idx]

        elif order == "D":
            pass
        elif order == "U":
            number = int(c.split()[1])
            for _ in range(number):
                now_idx = up[now_idx]

        elif order == "D":
            number = int(c.split()[1])
            for _ in range(number):
                now_idx = down[now_idx]




    pass

    
  

if __name__ == "__main__":
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    # "OOOOXOOO"
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
    # "OOXOXOOO"
    