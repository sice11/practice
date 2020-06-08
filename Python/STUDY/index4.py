# 8 while文
time = 60
while time > 0:
    print("残り",time,"sです。")
    time -= 1
    if time == 30:
        continue
    elif time < 5:
        break
print("時間切れです。")

# breakは繰り返し処理を終了させる
# continueは処理を"スキップ"して、次の処理へと進む