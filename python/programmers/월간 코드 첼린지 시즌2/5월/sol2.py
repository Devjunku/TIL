def is_equal(a, b):
    cnt = 0
    a = list(a)
    b = list(b)
    for ae, be in zip(a, b):
        if ae != be:
            cnt += 1
            if cnt == 3:
                return None

    return cnt


def solution(numbers):
    
    ans = []
    for n in numbers:
        
        n_bit = list(bin(n)[2:])
        n_len = len(n_bit)
        i = n + 1

        if n_bit[n_len-1] == '0':
            n_bit[n_len-1] = '1'
            ele = int(''.join(n_bit), 2)
            ans.append(ele)
            continue

        one_n = 0
        for b in n_bit:
            if b == '1':
                one_n += 1

        if one_n == n_len:
            n_bit[0] = '0'
            n_bit = ['1'] + n_bit 
            ele = int(''.join(n_bit), 2)
            ans.append(ele)
            continue

        while True:

            i_bit = bin(i)[2:]
            i_len = len(i_bit)

            if n_len < i_len:
                n_bit = n_bit.zfill(i_len)
                cnt = is_equal(n_bit, i_bit)
            else:
                cnt = is_equal(n_bit, i_bit)

            if cnt != None:
                break
        
            i += 1
    
        ans.append(i)

    return ans


if '__main__' == __name__:
    print(solution([2,7]))
    print(solution([15, 31]))