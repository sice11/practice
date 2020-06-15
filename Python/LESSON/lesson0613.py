# print("Hellow World")

list = [1,2,3,4,5,6,7,8,9,10]
# num = 0
# while num < 10 :
#     if list[num] == 3:
#         print(list[num],"だよ")
#     elif list[num] == 5:
#         print(list[num],"だよ")
#     else:
#         print(list[num])
#     num += 1

# for i in list:
#     if i == 3:
#         print(i,"だよ")
#     elif i == 5:
#         print(i,"だよ")
#     else:
#         print(i)

# 上の見本
# strはなくてもいいが、古いバージョンだと必要
# for l in list:
#     if l == 3 or l == 5:
#         print("{}だよ".format(str(l)))
#     else:
#         print(l)

# def lesson():
#     list1 = [1,2,3,4,5,6,7,8,9,10]
#     for l in list1:
#         if l == 3 or l == 5:
#             print("{}だよ".format(str(l)))
#         else:
#             print(l)
# lesson()

class lesson:
    list1 = [1,2,3,4,5,6,7,8,9,10]
    def lesson_func():
        for l in lesson.list1:
            if l == 3 or l == 5:
                print("{}だよ".format(l))
                # print("{}だよ".format(str(l)))
            else:
                print(l)
lesson.lesson_func()


# 条件文・繰り返し文はクラスの中の関数に入れる。
# 変数や配列はクラスやメソッドの中に入れる。