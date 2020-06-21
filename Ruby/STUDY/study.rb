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
data2 = Array.new(3)
data2 = [
    "toto",
    "ka-ten",
    "sakana",
    "usi"
]
# puts data2.length
puts data2[0,3]