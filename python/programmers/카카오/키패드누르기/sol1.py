def distance(left, right, ob, hand):
    lx, ly = left
    rx, ry = right
    obx, oby = ob

    l_d = abs(obx-lx) + abs(oby-ly)
    r_d = abs(obx-rx) + abs(oby-ry)

    if l_d > r_d:
        return 'R'
    elif l_d < r_d:
        return 'L'
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'

def solution(numbers, hand):

    hand_dic = {
        1:(0, 3),
        4:(0, 2),
        7:(0, 1),
        '*': (0, 0),
        2:(1, 3),
        5:(1, 2),
        8:(1, 1),
        0:(1, 0),
        3:(2, 3),
        6:(2, 2),
        9:(2, 1),
        '#':(2, 0)
    }

    answer = []
    l_l = [(0, 0)]
    r_l = [(2, 0)]
    for number in numbers:
        if number in [1, 4, 7]:
            answer.append("L")
            l_l.pop()
            l_l.append(hand_dic[number])
        elif number in [3, 6, 9]:
            answer.append("R")
            r_l.pop()
            r_l.append(hand_dic[number])
        else:
            res = distance(l_l[-1], r_l[-1], hand_dic[number], hand)
            answer.append(res)
            if res == 'L':
                l_l.pop()
                l_l.append(hand_dic[number])
            else:
                r_l.pop()
                r_l.append(hand_dic[number])

    return "".join(answer)

if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))