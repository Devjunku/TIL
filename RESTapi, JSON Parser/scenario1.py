import requests, json, time, sys
from random import shuffle
from pprint import pprint
'''
0: 6초간 아무것도 하지 않음
1: 위로 한 칸 이동 , tx - x < 0
2: 오른쪽으로 한 칸 이동 , ty - y > 0
3: 아래로 한 칸 이동 , tx - x > 0
4: 왼쪽으로 한 칸 이동,  ty - y < 0
5: 자전거 상차
6: 자전거 하차
'''
# direct = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}
def carry_bike(value, even_odd):
    lim = value["loaded_bikes_count"]
    res = []
    x, y = 4-value["location_id"]%5, value["location_id"]//5

    s = 0
    i = 0
    for i in range(4):
        s += bike[x][i]
        if bike[x][i]:
            i += 1
    
    mean = min(int(s/i), 2)

    if even_odd % 2:
        if lim > 5:
            if x == 0:
                res.append(2)
                res.append(6)
                res.append(6)
                res.append(6)
                lim -= 3
                res.append(4)
            elif x != 0 and x != 4:
                res.append(4)
                res.append(6)
                lim -= 1
                res.append(2)
                res.append(2)
                res.append(6)
                lim -= 1       
                res.append(4)
            else:
                res.append(4)
                res.append(6)
                res.append(6)
                res.append(6)
                lim -= 3
                res.append(2)
        while len(res) < 10 and x != 0: # 위로 올라가
            if lim > 0:
                res.append(6)
                lim -= 1
            if bike[x][y] > mean + 1:
                while bike[x][y] > mean + 1:
                    res.append(5)
                    lim += 1
                    bike[x][y] -= 1
                    if len(res) == 10:
                        return res
            elif bike[x][y] < mean:
                while bike[x][y] < mean and lim > 0:
                    res.append(6)
                    bike[x][y] += 1
                    lim -= 1
                    if len(res) == 10:
                        return res
            x -= 1
            res.append(1)

    else:
        if lim > 5:
            if x == 0:
                res.append(2)
                res.append(6)
                res.append(6)
                res.append(6)
                lim -= 3
                res.append(4)
            elif x != 0 and x != 4:
                res.append(4)
                res.append(6)
                lim -= 1
                res.append(2)
                res.append(2)
                res.append(6)
                lim -= 1       
                res.append(4)
            else:
                res.append(4)
                res.append(6)
                res.append(6)
                res.append(6)
                lim -= 3
                res.append(2)
        while len(res) < 10 and x != 4: # 아래로 내려가
            if bike[x][y] == 0 and lim > 0:
                res.append(6)
                lim -= 1
            if bike[x][y] > mean + 1:
                while bike[x][y] > mean  + 1:
                    res.append(5)
                    lim += 1
                    bike[x][y] -= 1
                    if len(res) == 10:
                        return res
            elif bike[x][y] < mean:
                while bike[x][y] < mean and lim > 0:
                    res.append(6)
                    bike[x][y] += 1
                    lim -= 1
                    if len(res) == 10:
                        return res
            x += 1
            res.append(3)

    return res
    

BASE_URL="https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

def start():
    x_auth_token = "d4986bbc32dc9fbbd941a7bbf1006829"
    headers = {"X-Auth-Token": x_auth_token}
    data = {"problem": 1}
    start_json = requests.post(BASE_URL+"/start", headers = headers, data=data).json()
    return start_json


def locations(auth_key):
    headers = {"Authorization": auth_key}
    trucks_json = requests.get(BASE_URL+"/locations", headers=headers).json()
    return trucks_json


def trucks(auth_key):
    headers = {"Authorization": auth_key}
    trucks_json = requests.get(BASE_URL+"/trucks", headers=headers).json()
    return trucks_json

# 초기 트럭을 위치시키기
def go_truck(truct_len):
    go = []
    for i in range(truct_len):
        truck_field = [0 for _ in range(truct_len)]
        if i > 0:
            for j in range(0,i):
                truck_field[j] = 2
        go.append(truck_field)
    return go


# 가장 최소값을 지닌 필드 찾기
def find_minimum(bike):
    min_v = sys.maxsize
    mini_field = []
    for i in range(5):
        for j in range(5):
            if min_v > bike[i][j]:
                min_v = bike[i][j]
        
    for i in range(5):
        for i in range(5):
            if min_v == bike[i][j]:
                mini_field.append((i, j))
    return mini_field.sort()


def bike_location(locations_json):
    field = []
    for data in locations_json["locations"]:
        field.append((4-data["id"]%5, data["id"]//5))
        bike[4-data["id"]%5][data["id"]//5] = data["located_bikes_count"]

    return field

def simulate(auth_key, data):
    headers = {"Authorization": auth_key}
    simulate_json = requests.put(BASE_URL+"/simulate", headers=headers, data=data).json()
    return simulate_json


def score(auth_key):
    headers = {"Authorization": auth_key}
    score_json = requests.get(BASE_URL+"/score", headers=headers).json()
    return score_json


if __name__ == "__main__":
    # 초기
    bike = [[0 for _ in range(5)] for _ in range(5)]

    # 스타트
    start_json = start()
    
    # 자전거 정보 갖고오기
    locations_json = locations(start_json["auth_key"])

    # 트럭 정보 갖고오기
    trucks_json = trucks(start_json["auth_key"])
    
    # 트럭의 위치 정보를 통해 특정 구역으로 보내기
    init_command = go_truck(len(trucks_json["trucks"]))

    # 데이터 세팅
    data = {
                "commands": []
            }
    
    # 초기 트럭을 해당 지역으로 보내기
    for idx, value in enumerate(init_command):
        data["commands"].append({"truck_id": idx, "command": value})

    # 시작!
    for _ in range(720):

        # dictionary json으로 변환
        data = json.dumps(data)

        # 시뮬레이션 go go
        res = simulate(start_json["auth_key"], data)
        even_odd = res["time"]
        pprint(res)
        # 자전거 정보 받기 
        locations_json = locations(start_json["auth_key"])

        # 자전거 정보 업데이트
        bike_location(locations_json)
        # mini_field = find_minimum(bike)
        trucks_json = trucks(start_json["auth_key"])
        pprint(trucks_json)
        if res["status"] == "finished":
            break
        time.sleep(0.1)

        data = {
                "commands": []
            }

        for truck in trucks_json["trucks"]:
            d = carry_bike(truck, even_odd)
            data["commands"].append({"truck_id": truck["id"], "command": d})
            mini_field = find_minimum(bike)
        pprint(bike)
        pprint(data)
    res = score(start_json["auth_key"])
    pprint(res)
