# 演習1
# list = [1,1,2,3,3,4,5,4,6]
# print(set(list))

# 演習2
# d = {}
# input_word = input()
# word_list = input_word.split(" ")
# if word_list[0] == "save":
#     d[word_list[1]] = word_list[2]
#     print(d)
# elif word_list[0] == "get":
#     print(d[word_list[1]])
# else:
#     print("Error")
d = {}
for k,v in d.items():
    input_word = input()
    word_list = input_word.split(" ")
    if (word_list[0] == "save" and len(word_list) == 3):
        k = word_list[1]
        v = word_list[2]
        d[k] = v
    elif (word_list[0] == "get" and len(word_list) == 2):
        k = word_list[1]
        if k in d:
            print(d[k])
        else:
            print("Error")
    else:
        print("Input Error")
