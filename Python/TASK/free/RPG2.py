import random

# 属性の設定
attribute = ["火","水","雷"]

# 各ステータスの元を作成
class Status:
    def __init__(self,name,hp,attack,attribute):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.attribute = random.randint(0,2)
    def __call__(self):
        print("{}属性で{}の攻撃".format(self.attribute,self.attack))

hiro = Status("hiro",120,random.randint(20,40),attribute)
print(hiro())