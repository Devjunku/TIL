def solution(n, arr1, arr2):
    ans = []
    for a1, a2 in zip(arr1, arr2):
        res1 = bin(a1)[2:].zfill(n)
        res2 = bin(a2)[2:].zfill(n)
        temp = ''
        for r1, r2 in zip(res1, res2):
            if r1 == '0' and r2 == '0':
                temp += ' '
            else:
                temp += '#'
        ans.append(temp)

    return ans


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))