# 演習1
# リストから重複を取り除く関数を、setを使って作成
# list = [1,2,2,3,4,4]

# list_set = set(list)

# print(list_set)


# 演習2
# grade = {
#     "tanaka":70,
#     "yoshioka":80,
#     "mirai":50
# }
d = {}

while(True):
    line = input()
    words = line.split()

    if(words[0] == 'save' and len(words) == 3):
        key = words[1]
        value = words[2]
        d[key] = value
        print(d)

    elif(words[0] == 'get' and len(words) == 2):
        key = words[1]
        if key in d:
            print(d[key])
        else:
            print('Error')

    else:
        print('Input Error')