import requests
import csv
import json
import pprint

# レストラン検索APIのURL
URL = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

keyid_input = input()

# リクエストパラメータの設定
params = {}
# keyidは後に外部入力にする
params["keyid"] = keyid_input
params["hit_per_page"] = 20
# 以下のフリーワードも外部入力
params["freeword"] = "大阪駅,魚"

# URLにリクエストする
json_response = requests.get(URL,params).text
# json形式のレスポンスをパース（変換）して、辞書型にする。
res = json.loads(json_response)

restaurants = res["rest"]

# csv出力
with open("restaurants_list.csv","a",newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(restaurants)
print(restaurants)