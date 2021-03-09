# 페이스북 문제

string = input()

str_list = []
int_list = 0
for s in string:
    if s.isdigit():
        int_list += int(s)
    else:
        str_list.append(s)
str_list.sort()
str_list.append(str(int_list))
print(''.join(str_list))


