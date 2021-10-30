# sol!!!

from math import ceil

def timetomin(time):
    h, m = time.split(":")
    return 60 * int(h) + int(m)

def solution(fees, records):

    in_out_dic = {}
    time_idc = {}
    answer_dic = {}
    for record in records:
        time, number, in_out = record.split()
        if number not in in_out_dic.keys():
            in_out_dic[number] = []
            time_idc[number] = []
            answer_dic[number] = 0
        if in_out == "IN":
            in_out_dic[number].append("IN")
            time_idc[number].append(timetomin(time))
        else:
            in_out_dic[number].pop()
            intime = time_idc[number].pop()
            outtime = timetomin(time)
            answer_dic[number] += (outtime - intime)

    for key in in_out_dic.keys():
        if "IN" in in_out_dic[key]:
            intime = time_idc[key].pop()
            answer_dic[key] += timetomin("23:59") - intime
        
    answer_dic = sorted(answer_dic.items())
    answer = []
    for key, value in answer_dic:
        if value > fees[0]:
            answer.append(fees[1] + ceil((value-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])

    return answer


if __name__ == "__main__":
    print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
    print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
    print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))