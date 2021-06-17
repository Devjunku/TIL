skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        cn = 0
        indx = []
        for sk in skill_tree:
            if sk in skill:
                indx.append(skill.index(sk))
        for i in range(len(indx)):
            if indx[i] == i:
              cn += 1
        if cn == len(indx):
            cnt += 1
    return cnt   
     
print(solution(skill, skill_trees))


        



