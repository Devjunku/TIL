current_time = input()
drow_time = input()

def time_to_second(time):
    hh, mm, ss = map(int, time.split(":"))
    return 60*60*hh + 60*mm + ss

def time_to_hour(second):
    hh, mod = divmod(second, 3600)
    hh = str(hh).zfill(2)
    mm, ss = divmod(mod, 60)
    mm = str(mm).zfill(2)
    ss = str(ss).zfill(2)
    return ":".join([hh, mm, str(ss)])

if time_to_second(current_time) == time_to_second(drow_time):
    print("00:00:01")
elif 86400 - time_to_second(current_time) + time_to_second(drow_time) < 86400:
    ans_s = 86400 - time_to_second(current_time) + time_to_second(drow_time)
    answer = time_to_hour(ans_s)
    print(answer)
else:
    ans_s = time_to_second(drow_time) - time_to_second(current_time)
    answer = time_to_hour(ans_s)
    print(answer)