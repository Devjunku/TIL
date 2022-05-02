from collections import defaultdict

def solution(string):

    dic = defaultdict(int)
    elem = ""
    for s in string:
        if s.isdecimal():
            elem += s
        else:
            if elem.isdecimal():
                dic[elem] += 1
            elem = ""
    
    dic = list(dic.items())
    dic.sort(key=lambda x: x[1], reverse=True)
    answer = []

    for k, v in dic:
        answer.append(int(k))
    
    return answer


        
    

if __name__ =="__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution("{{20,111},{111}}"))
    print(solution("{{123}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))