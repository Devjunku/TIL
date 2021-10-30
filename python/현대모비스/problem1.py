from typing_extensions import ParamSpecKwargs


from itertools import permutations

def solution(dice):
    total = []
    for d in dice:
        total += d

    N = len(dice)

    nn_list = list(range(1, 10**N))

    make = []
    for n in range(1, N+1):
        for i in list(permutations(total, n)):
            num = int("".join(map(str, list(i))))
            if num in make:
                continue
            else:
                make.append(int("".join(map(str, list(i)))))
                
    s_num = sorted(make)[1:]
    for idx, n in enumerate(s_num):
        if (idx+1) != n:
            return idx+1
            
if __name__ == "__main__":
    print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))
    print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]))