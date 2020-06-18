# restaurants_searcher.py

import json
import csv
import requests

input_KEYID = input()

# 初期設定
KEYID = input_KEYID
HIT_PER_PAGE = 100
PREF = "PREF13"
FREEWORD_CONDITION = 1
FREEWORD = "渋谷駅"

PARAMS = {"keyid": KEYID, "hit_per_page":HIT_PER_PAGE, "pref":PREF, "freeword_condition":FREEWORD_CONDITION, "freeword":FREEWORD}

def write_data_to_csv(params):
    restaurants = []
    json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/", params=params).text
    response = json.loads(json_res)
    if "error" in response:
        return print("エラーが発生しました！")
    for restaurant in response["rest"]:
        restaurant_name = restaurant["name"]
        restaurants.append(restaurant_name)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)