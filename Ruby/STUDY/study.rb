# 5章 配列
# customer = [
#     "samurai",
#     "zirou",
#     "toto"
# ]

# customer.each do |customer|
#     puts customer
# end
# puts customer[0]

# 配列の作成の仕方
# ①Array.newを使う
# data = Array.new(["satou","yamada","umiushi"])
# puts data[-1]
# ②いつも通り、[ ]を活用
# また、配列の大きさを指定することもできる。
# data2 = Array.new(3)
# data2 = [
#     "toto",
#     "ka-ten",
#     "sakana",
#     "usi"
# ]
# # puts data2.length
# puts data2[0,3]

# data = Array.new(10,["hoge","fuge"])
# # puts data
# d = data.uniq
# puts d

# 6章 ifを使った条件分岐
def num
    40.upto(50){|i|
    if i == 42
        puts "Answer to the Ultimate Question of Life, the Universe, and Everything"
    else
        puts i
    end
    }
end
num