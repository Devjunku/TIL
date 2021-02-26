def d_mat(arr):

    N = len(arr)//2

    d_arr = []

    for i in range(N):
        de_arr = []
        for j in range(N):
            de_arr.append(arr[i][j])
        d_arr.append(de_arr)

    for i in range(N):
        de_arr = []
        for j in range(N, len(arr)):
            de_arr.append(arr[i][j])
        d_arr.append(de_arr)

    for i in range(N, len(arr)):
        de_arr = []
        for j in range(N):
            de_arr.append(arr[i][j])
        d_arr.append(de_arr)

    for i in range(N, len(arr)):
        de_arr = []
        for j in range(N, len(arr)):
            de_arr.append(arr[i][j])
        d_arr.append(de_arr)

    return d_arr

def merge_d(n_arr):
    N = len(n_arr)//4
    res_arr = []
    for i in range(0, len(n_arr), N):
        conf = []
        for j in range(i, i+N):
            conf += n_arr[j]
        if conf.count(0) == 0:
            res_arr.append([1])
        elif conf.count(1) == 0:
            res_arr.append([0])
        else:
            for j in range(i, i+N):
                res_arr.append(n_arr[j])
    return res_arr

def pop_con(res_arr):
    single_list = []
    multi_list = []
    for i in range(len(res_arr)):
        if len(res_arr[i]) == 1:
            single_list.extend(res_arr[i])
        else:
            multi_list.append(res_arr[i])

    return single_list, multi_list


def solution(arr):
    # print(pop_con(merge_d(d_mat(arr))))
    zero_list = []
    one_list = []
    while True:
        single_list, multi_list = pop_con(merge_d(d_mat(arr)))

        for i in range(len(single_list)):
            if single_list[i] == [0]:
                zero_list.extend([0])
            else:
                one_list.extend([1])
        
        arr = multi_list
        if len(multi_list[0]) < 4:
            break
    print(zero_list, one_list)
        

        
         







    
    # 최종 결과
    # zero_c = 0
    # one_c = 0
    # for s in range(len(arr)):
    #     zero_c += s.count(0)
    #     one_c += s.count(1)

    # print([zero_c, one_c])





if __name__ == '__main__':
    print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
    print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))