from collections import defaultdict

def dfs(name, am):
    global benefit_dic, dadange

    if am == 0: return

    mine, recommend_people = am - int(am / 10), int(am / 10)
    benefit_dic[name] += mine

    for rec in dadange[name]: dfs(rec, recommend_people)


def solution(enroll, referral, seller, amount):
    global benefit_dic, dadange
    
    benefit_dic = defaultdict(int)
    dadange = defaultdict(list)

    benefit_dic["center"]
    dadange["center"]

    for en, re in zip(enroll, referral):
        if re != "-":
            dadange[en].append(re)
        else:
            dadange[en].append("center")
        benefit_dic[en]
        

    for sell, am in zip(seller, amount):
        dfs(sell, am*100)

    return [benefit_dic[i] for i in enroll]

if __name__ == "__main__":
    print(
        solution(
            ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
            ["young", "john", "tod", "emily", "mary"],
            [12, 4, 2, 5, 10]
        )
    )
    # [360, 958, 108, 0, 450, 18, 180, 1080]
    print(
        solution(
            ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
            ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
            ["sam", "emily", "jaimie", "edward"],
            [2, 3, 5, 4]
        )
    )
    # [0, 110, 378, 180, 270, 450, 0, 0]