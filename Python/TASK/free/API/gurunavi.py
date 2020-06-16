import requests
import json
import csv
import pprint

url = ""

# リクエストパラメータの設定（辞書型で）
params = {}
params["keyid"] = "64270ef5e2cf61749e8c579c2f6c4084"
params["freeword"] = "大阪駅,魚"

# urlにparamsで設定した情報を投げる その情報をresponse変数に格納
response = requests.get(url,params)
# どんな値が入っているのかの確認
# pprint.pprint(response.json())
# responseのままだと、辞書型の値が見にくいので、別の変数に置き換える
results = response.json()
restaurants = results["rest"]
print(pprint.pprint(restaurants[0]))