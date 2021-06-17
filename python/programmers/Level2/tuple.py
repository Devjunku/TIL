dat = "{{123}}"
dat = ''.join(dat.split('}'))
dat = ''.join(dat.split('{'))
dat = list(map(int, dat.split(',')))

print(dat)

N = len(set(dat))

res_list = []
for i in range(N, 0, -1):
    for j in list(set(dat)):
        if dat.count(j) == i:
            res_list.append(j)
print(res_list)

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter


