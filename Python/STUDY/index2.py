#4 classについて
class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    
    def __call__(self):
        print("ここは{}のcall関数です。".format(self.name))

    # 新たに一つformat関数を使って作成している
    def greeting(self,name):
        print("こんにちは、{}さん。私は、{}と申します。".format(name,self.name))


tarou = Person("tarou",17,"nara")
yamada = Person("yamada",52,"hokkaido")

# call関数の実行 実行方法が特別
# tarou()

yamada.greeting("nakano")

