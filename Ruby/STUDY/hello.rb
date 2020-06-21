# puts "Hello World!"

# puts "Hello Ruby!"

# 第二章
# str = "Hello World!"
# puts str

# name = "Sice"
# puts name

# class Hoge
#     def num
#         @@num_num = 4 * 5
#         puts @@num_num
#     end
# end
# hoge = Hoge.new
# puts hoge.num

# 3章
# def show(a)
#     puts a
# end
# a = "Ruby Work"
# show(a)

# def show(work = "Hello")
#     puts work
# end
# show
# show("42")

# def calc (a,b)
#     puts a*b
# end

# calc(5,6)

# 4章 クラス
# num = 42
# a = 42
# puts num

# class name_func
#     def talk
#         puts "Hellow"
#     end
# end

# hello = name_func.new
# hello.talk

# puts "Hello " + "World"

# str = String.new("45")
# puts str

# name = [
#     "suzuki",
#     "tanaka",
#     "katou",
#     "icnirou"
# ]

# puts name[-2]

# profile = Hash.new
# profile[:name] = "suzuki"
# profile[:age] = 27
# puts profile[:age]

# profile = {
#     :name => "suzuki",
#     :age => 50
# }

# puts profile[:age]

class Hoge
    def hello
        puts "Hello Ruby"
    end
end

hello_puts = Hoge.new
hello_puts.hello

class Hoge2 < Hoge
    def hello2
        puts "Hello World"
    end
end

hello2_puts = Hoge2.new
hello2_puts.hello
hello2_puts.hello2