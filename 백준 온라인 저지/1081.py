L, U = map(int, input().split())

num_list = list(map(str,range(L, U+1)))
num_list =''.join(num_list)
sum_dat = 0
for num in num_list:
    sum_dat += int(num)
print(sum_dat)