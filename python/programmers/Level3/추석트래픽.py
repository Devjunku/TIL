def end(time):
    split_time = time.split(":")
    second_m = split_time[2].split(".")
    return int(split_time[0]) * 3600 * 1000 + int(split_time[1]) * 60 * 1000 + int(second_m[0]) * 1000 + int(second_m[1])
    

def start(start_time, ing):
    return start_time - int(float(ing[:-1]) * 1000) + 1


def solution(lines):
    
    start_times = []
    end_times = []

    answer = 0

    for line in lines:
        times = line.split()
        end_times.append(end(times[1]))
        start_times.append(start(end(times[1]), times[2]))

    for i in range(len(start_times)):
        cnt = 0
        for j in range(i, len(start_times)):
            if end_times[i] > start_times[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer

if __name__ == "__main__":
    print(solution(["2016-09-15 01:00:04.002 2.0s",
                    "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 20:59:57.421 0.351s",
                    "2016-09-15 20:59:58.233 1.181s",
                    "2016-09-15 20:59:58.299 0.8s",
                    "2016-09-15 20:59:58.688 1.041s",
                    "2016-09-15 20:59:59.591 1.412s",
                    "2016-09-15 21:00:00.464 1.466s",
                    "2016-09-15 21:00:00.741 1.581s",
                    "2016-09-15 21:00:00.748 2.31s",
                    "2016-09-15 21:00:00.966 0.381s",
                    "2016-09-15 21:00:02.066 2.62s"]))