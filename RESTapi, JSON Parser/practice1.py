import requests, json, time
from pprint import pprint

BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

def start():
    headers = {
        "X-Auth-Token": "d4986bbc32dc9fbbd941a7bbf1006829"
    }
    data = {
        "problem": 1
    }
    res = requests.post(BASE_URL+"/start", headers=headers, data=data).json()
    return res


def locations(auth_key):
    headers = {"Authorization": auth_key}
    trucks_json = requests.get(BASE_URL+"/locations", headers=headers).json()
    return trucks_json

def trucks(auth_key):
    headers = {"Authorization": auth_key}
    trucks_json = requests.get(BASE_URL+"/trucks", headers=headers).json()
    return trucks_json


def simulate(auth_key, data):
    headers = {
        "Authorization": auth_key
    }
    res = requests.put(BASE_URL+"/simulate", headers=headers, data=data).json()
    return res

def score(auth_key):
    headers = {"Authorization": auth_key}
    score_json = requests.get(BASE_URL+"/score", headers=headers).json()
    return score_json

'''
0: 6초간 아무것도 하지 않음
1: 위로 한 칸 이동
2: 오른쪽으로 한 칸 이동
3: 아래로 한 칸 이동
4: 왼쪽으로 한 칸 이동
5: 자전거 상차
6: 자전거 하차
'''

def movie_trucks(fields, locations_info, trucks_info):
    locations_info = locations_info
    print("--------------------------")
    
    trucks_info = trucks_info
    
    data = {
        "commands": []
    }

    for i in range(5):
        
        moving_truck = {
            "truck_id": i,
            "command": []
            }
        idx = trucks_info[i]["location_id"]
        print(idx)
        x, y = 4 - idx%5, idx//5
        # print(x, y)
        if idx in [0, 5, 10, 15, 20]:          
            while moving_truck["command"].count(1) < 4:
                if fields[x][y] == 0 and trucks_info[i]["loaded_bikes_count"] > 0:
                    moving_truck["command"].append(6)
                    fields[x][y] += 1
                    trucks_info[i]["loaded_bikes_count"] -= 1

                while fields[x][y] < 2 and trucks_info[i]["loaded_bikes_count"] > 0:
                    moving_truck["command"].append(6)
                    fields[x][y] += 1
                    trucks_info[i]["loaded_bikes_count"] -= 1

                if fields[x][y] > 2 and trucks_info[i]["loaded_bikes_count"] < 10:
                    moving_truck["command"].append(5)
                    fields[x][y] -= 1
                    trucks_info[i]["loaded_bikes_count"] += 1

                while fields[x][y] > 3:
                    moving_truck["command"].append(5)
                    fields[x][y] -= 1
                    trucks_info[i]["loaded_bikes_count"] += 1
                
                x = x-1
                moving_truck["command"].append(1)
                
        elif idx in [4, 9, 14, 19, 24]:
            while moving_truck["command"].count(3) < 4:
                if fields[x][y] == 0 and trucks_info[i]["loaded_bikes_count"] > 0:
                    moving_truck["command"].append(6)
                    fields[x][y] += 1
                    trucks_info[i]["loaded_bikes_count"] -= 1

                while fields[x][y] < 2 and trucks_info[i]["loaded_bikes_count"] > 0:
                    moving_truck["command"].append(6)
                    fields[x][y] += 1
                    trucks_info[i]["loaded_bikes_count"] -= 1
                
                if fields[x][y] > 2 and trucks_info[i]["loaded_bikes_count"] < 10:
                    moving_truck["command"].append(5)
                    fields[x][y] -= 1
                    trucks_info[i]["loaded_bikes_count"] += 1

                while fields[x][y] > 4:
                    moving_truck["command"].append(5)
                    fields[x][y] -= 1
                    trucks_info[i]["loaded_bikes_count"] += 1
                
                x = x+1
                moving_truck["command"].append(3)

        data["commands"].append(moving_truck)
    pprint(data)
    return data

    
if __name__ == "__main__":
    # 키 시작
    start_json = start()
    auth_key = start_json["auth_key"]

    # 자전거 정보 받기
    locations_json = locations(start_json["auth_key"])
    locations_info = locations_json["locations"]

    # 초기 자전거 정보 array에 기록
    fields = [[0 for _ in range(5)] for _ in range(5)]
    for l in locations_info:
        idx = l["id"]
        fields[4-idx%5][idx//5] = l["located_bikes_count"]

    # 트럭 정보 받기
    trucks_json = trucks(start_json["auth_key"])
    trucks_info = trucks_json["trucks"]
    pprint(trucks_info)
    # 데이터 세팅
    data = {
        "commands": []
    }

    # 초기 트럭 위치시키기
    for truck in trucks_info:
        init_command = {   
                "truck_id": truck["id"],
                "command": [0]+[2 for _ in range(int(truck["id"]))]
            }
        data["commands"].append(init_command)

    pprint(data)
    data = json.dumps(data)
    simulate_info = simulate(start_json["auth_key"], data)
    pprint(simulate_info)

    for _ in range(720):
        time.sleep(0.1)

        # 자전거 정보 받기
        locations_json = locations(start_json["auth_key"])
        locations_info = locations_json["locations"]
        # pprint(locations_info)

        # 받은 자전거 데이터 다시 field에 반영
        for l in locations_info:
            idx = l["id"]
            fields[4-idx%5][idx//5] = l["located_bikes_count"]
        pprint(fields)
        # 트럭 정보 받기
        trucks_json = trucks(start_json["auth_key"])
        trucks_info = trucks_json["trucks"]
        pprint(trucks_info)
        # 명령어 받기
        data = movie_trucks(fields, locations_info, trucks_info)

        # dictionary -> json dumps
        data = json.dumps(data)
        simulate_info = simulate(start_json["auth_key"], data)
        pprint(simulate_info)

        if simulate_info["status"] != "ready":
            score_json = score(start_json["auth_key"])
            print(score_json)
            break

        
        




