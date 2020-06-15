# 演習1
# list = [[1,5,3],[2,6,4]]
# print(max(list[0]))
# print(max(list[1]))

# 演習2
n = 1
for i in range(1,100):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    n += 1