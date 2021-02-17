dats = [i for i in range(1, 10001)]

for dat in range(1, 10001):
    initiN = [dat]
    eles = list(str(dat))

    for ele in eles:
        abss = int(ele)
        initiN.append(abss)

    sum_ini = sum(initiN)
    if sum_ini in dats:
        dats.remove(sum_ini)

for dat in dats:
    print(dat)