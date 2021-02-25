from sys import stdin

N = int(stdin.readline().rstrip())



def solution(a_dict, b_dict):

    if a_dict[4] > b_dict[4]:
        return 'A'
    elif a_dict[4] < b_dict[4]:
        return 'B'
    elif a_dict[4] == b_dict[4]:
        if a_dict[3] > b_dict[3]:
            return 'A'
        elif a_dict[3] < b_dict[3]:
            return 'B' 
        elif a_dict[3] == b_dict[3]:
            if a_dict[2] > b_dict[2]:
                return 'A'
            elif a_dict[2] < b_dict[2]:
                return 'B' 
            elif a_dict[2] == b_dict[2]:
                if a_dict[1] > b_dict[1]:
                    return 'A'
                elif a_dict[1] < b_dict[1]:
                    return 'B' 
                elif a_dict[1] == b_dict[1]: 
                    return 'D'

for _ in range(N):
    a_list = list(map(int,stdin.readline().rstrip().split()))
    b_list = list(map(int,stdin.readline().rstrip().split()))
    a_num = a_list[0]
    a_ddak = a_list[1:]
    b_num = b_list[0]
    b_ddak = b_list[1:]

    a_dict = {
        4: 0,
        3: 0,
        2: 0,
        1: 0
        }

    b_dict = {
        4: 0,
        3: 0,
        2: 0,
        1: 0
        }
    
    for a_dd in a_ddak:
        a_dict[a_dd] += 1
    
    for b_dd in b_ddak:
        b_dict[b_dd] += 1
    
    # print(a_dict[4])
    # print(b_dict[4])


    # print(a_dict, b_dict)

    print(solution(a_dict, b_dict))
    
    

    