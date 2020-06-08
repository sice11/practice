# sum = 0
# for i in range(1,21):
#     sum += i
# print(sum)

# 課題
# for num in range(1,31):
#     if num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# for num2 in range(1,31,2):
#     print(num2)

# リストから、順番に取り出すとき
# names = ["yamada","tanaka","miura","kitou"]
# for name in names:
#     print("Mr." + name)

# zip関数
first_names = ["Alisa","Morishima"]
midle_names = ["Ilinichina","Lovely"]
last_names = ["Amiella","Haruka"]
# for first_name,midle_name,last_name in zip (first_names,midle_names,last_names):
#     print(first_name + "・" + midle_name + "・" + last_name)

# enumerate関数 要素番号と要素の値を取り出す。
for banngou,last_name in enumerate (last_names):
    print("出席番号" , banngou , "番目の" , last_name , "さん")