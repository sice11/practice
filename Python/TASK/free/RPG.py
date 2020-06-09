import random

# 登場人物のHPを作成
hiro = 100
enemy = 120

# お互いの属性と攻撃力を定義
hiro_ak = random.randint(20,40)
enemy_ak = random.randint(10,30)

# 属性の設定
attribute = ["火","水","雷"]
i = random.randint(0,2)

hiro_at = attribute[i]
enemy_at = attribute[i]

# 戦闘
while(hiro < 0 or enemy < 0):
    print("")