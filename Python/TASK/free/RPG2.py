import random

# 属性の設定
attribute = ["火","水","雷"]
i = random.randint(0,2)

# 各ステータスの元を作成
class Status:
    def __init__(self,name,hp,attack,attribute):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.attribute = attribute[i]
    def __call__(self):
        print("{}が{}属性で{}の攻撃".format(self.name,self.attribute,self.attack))

#主人公と敵のステータスを入力
hiro = Status("hiro",120,random.randint(20,40),attribute)
enemy = Status("enemy",50,random.randint(10,25),attribute)

# 先行を主人公とする
# 以下から、戦闘を開始。どちらかのhpの値が0になるまで実行
while(hiro.hp > 0) or (enemy.hp > 0):

    # 属性値による優劣を決める
    # 属性値反映後の攻撃値を以下にする
    hiroAT = hiro.attack
    enemyAT = enemy.attack

    # hiroの攻撃値が0.5倍になるケースをまとめる
    if (hiro.attribute == "火" and enemy.attribute == "水") or (hiro.attribute == "水" and enemy.attribute == "雷") or (hiro.attribute == "雷" and enemy.attribute == "火"):
        (hiroAT * 0.5) and (enemyAT * 1.5)
    #hiroの攻撃値が1.5倍になるケースをまとめる
    elif (hiro.attribute == "水" and enemy.attribute == "火") or (hiro.attribute == "雷" and enemy.attribute == "水") or (hiro.attribute == "火" and enemy.attribute == "雷"):
        (hiroAT * 1.5) and (enemyAT * 0.5)
    # 等倍分
    else:
        (hiroAT * 1.0) and (enemyAT * 1.0)
    
    print("戦闘開始")

    # 主人公を先行
    # callメソッドの呼び出し
    hiro()
    enemy.hp -= hiroAT

    # 敵の後攻
    # callメソッドの呼び出し
    enemy()
    hiro.hp -= enemyAT

if hiro.hp > 0:
    print(hiro.name + "の勝ち")
else:
    print(enemy.name + "の勝ち")