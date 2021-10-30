# sol!!

def solution(id_list, report, k):
    
    report = list(set(report))
    id_dic = { id:{ i:0 for i in id_list } for id in id_list }
    id_d = {i: 0 for i in id_list}
    id_ans = {i: 0 for i in id_list}
    for re in report:
        ket, gil = re.split()
        id_d[gil] += 1
        id_dic[ket][gil] += 1
    
    for key in id_d:
        if id_d[key] >= k:
            for key1 in id_dic.keys():
                if id_dic[key1][key] > 0:
                    id_ans[key1] +=1
    answer = []
    for v in id_ans.values():
        answer.append(v)
    
    return answer




    

if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))