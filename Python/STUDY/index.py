#1
# print("Hellow World!")

#2
# name = "名前 と　苗字"
# print(name)

# num = 1
# print(num + num)

# def func():
#     print(name)
# func()

#3
# def func(str):
#     print(str)
# func("Hello World!")

# def func(a,b):
#     print(a * b)
# func(12,16)

# def calc(a,b):
#     print(a * b)
# calc(12,16)

#4
class Person:
    def __init__(self,name,nationality,age):
        self.name = name
        self.nationality = nationality
        self.age = age

Sice = Person("sice","japan",27)
print(Sice.age)