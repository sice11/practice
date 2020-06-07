class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def __call__(self):
        print("これは{}のcall関数です。".format(self.name))
    def greeting(self,name):
        print("こんにちは、{}さん。私は{}です。".format(name,self.name))
    
miyako = Person("miyako",27,"tokyo")
zyunpei = Person("zyunpei",30,"ibaraki")

# miyakoを私とし、
# callメソッドの名前と、greetingメソッドの「私」の名前を同一にする。

miyako()

miyako.greeting("zyunpei")