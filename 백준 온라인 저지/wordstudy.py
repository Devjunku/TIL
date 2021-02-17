word = input()
w_list = list(word)
upw = [i.upper() for i in w_list ]

upw_1 = sorted(list(set(upw)))

num = []
for ele_up in upw_1:
   Num = upw.count(ele_up) 
   num.append(Num)

zip_1 = zip(upw_1, num)
max_num = max(num)

count1 = 0
for i in num:
    if i == max_num:
        count1 += 1
        
if count1 > 1:
    print('?')
else:
    for idx, value in zip_1:
        if value == max_num:
            print(idx)

