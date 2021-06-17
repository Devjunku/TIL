string = "{{123}}"
def solution(string):
    str1  = ''.join(string.split('{'))
    str2  = ''.join(str1.split('}'))
    num_list = list(map(int, str2.split(',')))
    dic = {}
    for ele in num_list:
            dic[ele] = dic.get(ele, 0) + 1
    res_list = []
    for i in range(len(dic), 0, -1):
        for di in dic.keys():
            if dic[di] == i:
                res_list.append(int(di))
                break    
    return res_list

print(solution(string))
# print(string.split('{'))
# print(''.join(string.split('{')))
# str1  = ''.join(string.split('{'))
# print(str1.split('}'))
# str2  = ''.join(str1.split('}'))
# list(map(int, str2.split(',')))


# str_ob = ''
# for s in range(len(string)):
#     if string[s] == '{' or string[s] == '}':
#         continue
#     else:
#         str_ob += string[s]

# dic = {}
# for ele in str_ob:
#     if ele != ',':
#         dic[ele] = dic.get(ele, 0) + 1

# res_list = []
# for i in range(len(dic), 0, -1):
#     for di in dic.keys():
#         if dic[di] == i:
#             res_list.append(int(di))
#             break
# print(res_list)


