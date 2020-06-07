#5 if文の課題に付け足し

# random関数を使って、0~10の数値を出力
# 奇数の場合は、「奇数です。」
# 偶数の場合は、「偶数です。」と出力する。

# import random
# num = random.randint(0,10)
# if num % 2 == 0:
#     print("偶数です。")
# else:
#     print("奇数です。")


# a in b
# a not in bを活用した例題
str = ["文","字","列"]
str2 = "文"
if str2 in str:
    print("文という文字が入っている")
else:
    print("まったく同じ要素がない")

# 出力結果>>まったく同じ要素がない