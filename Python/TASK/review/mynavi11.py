# 演習1
# list = [1,1,2,3,3,4,5,4,6]
# print(set(list))

# 演習2
d = {}
input_word = input()
word_list = input_word.split(" ")
if word_list[0] == "save":
    d[word_list[1]] = word_list[2]
    print(d)
elif word_list[0] == "get":
    print(d[word_list[1]])
else:
    print("Error")
