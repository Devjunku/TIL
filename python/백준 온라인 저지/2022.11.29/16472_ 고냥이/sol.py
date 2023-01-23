import sys
from collections import defaultdict
sys = sys.stdin.readline

# left, right point를 사용하여
# 현재의 알바벳의 종류만을 기록하면서
# 주어진 N보다 작거나 같으면, right를 하나 더 증가
# 많으면, left를 증가시킨다.

# 이때 중요한게 left부터 right 사이의 알파벳의 갯수가 몇 개인지가 중요하게 된다.
# 사용할 수 있는 메모리도 많으니까. set으로 현재 알파벳을 기록해주자.

# 같은 부분을 계속 set으로 만들어 버리니까. 그게 문제인거 같은데


N = int(input())
cat_lang = list(input().strip())
cat_lang_len = len(cat_lang)

if N == 26:
    print(cat_lang_len)
    exit()

right = 0
left = 0
answer = 0
cat_lang_dic = defaultdict(int)
current_alpha_set = set(cat_lang[0])
cat_lang_dic[cat_lang[0]] += 1

while left <= right and right < cat_lang_len:
    if len(current_alpha_set) <= N:
        answer = max(answer, sum(cat_lang_dic.values()))
        right += 1
        if right < cat_lang_len:
            cat_lang_dic[cat_lang[right]] += 1
            current_alpha_set.add(cat_lang[right])
    else:
        cat_lang_dic[cat_lang[left]] -= 1
        if cat_lang_dic[cat_lang[left]] == 0:
            current_alpha_set.discard(cat_lang[left])
        left += 1
    
print(answer)