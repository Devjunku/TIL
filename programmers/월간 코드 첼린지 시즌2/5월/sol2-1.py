def solution(numbers):
    
    ans = []
    for n in numbers:
        bit = list(bin(n)[2:])
        l = len(bit)
        # print(bit)
        bit = bit[::-1]
        

        if bit[0] == '0':
            bit[0] = '1'
            # print(bit[::-1])
            ele = int(''.join(bit[::-1]), 2)
            ans.append(ele)
            continue
    
        one_n = 1

        for i in range(1, l):
            if bit[i] == '0':
                bit[i] = '1'
                bit[i-1] = '0'
                # print(bit[::-1])
                ele = int(''.join(bit[::-1]), 2)
                ans.append(ele)
                break
            else:
                one_n += 1
        
        if one_n == l:
            bit.append('1')
            bit[l-1] = '0'
            # print(bit[::-1])
            ele = int(''.join(bit[::-1]), 2)
            ans.append(ele)

    return ans

if '__main__' == __name__:
    print(solution([2, 19, 7]))
    print(solution([15, 27, 25]))