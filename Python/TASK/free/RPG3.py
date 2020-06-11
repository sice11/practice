import random

# 主人公と敵の体力を入力
hiro_hp = 120
enemy_hp = 200

print("戦闘開始")

# 先行を主人公とする
# 以下から、戦闘を開始。どちらかのhpの値が0になるまで実行
while (hiro_hp > 0 and enemy_hp > 0):

    # 属性の設定
    # 主人公の属性
    attributeH = ["火","水","雷"]
    h = random.randint(0,2)
    # 敵の属性
    attributeE = ["火","水","雷"]
    e = random.randint(0,2)


    #主人公の攻撃力と属性を入力
    class hiro:
        attack = random.randint(20,40)
        attribute = attributeH[h]

    # 敵の攻撃力と属性を入力
    class enemy:
        attack = random.randint(10,15)
        attribute = attributeE[e]


    # 属性値による優劣を決める
    # 属性値反映後の攻撃値を以下にする
    hiroAT = hiro.attack
    enemyAT = enemy.attack

    # hiroの攻撃値が0.5倍になるケースをまとめる
    if (hiro.attribute == "火" and enemy.attribute == "水") or (hiro.attribute == "水" and enemy.attribute == "雷") or (hiro.attribute == "雷" and enemy.attribute == "火"):
        (hiroAT == hiroAT * 0.5) and (enemyAT == enemyAT * 1.5)
    #hiroの攻撃値が1.5倍になるケースをまとめる
    elif (hiro.attribute == "水" and enemy.attribute == "火") or (hiro.attribute == "雷" and enemy.attribute == "水") or (hiro.attribute == "火" and enemy.attribute == "雷"):
        (hiroAT == hiroAT * 1.5) and (enemyAT == enemyAT * 0.5)
    # 等倍分
    else:
        (hiroAT == hiroAT * 1.0) and (enemyAT == enemyAT * 1.0)
    

    # 主人公を先行
    enemy_hp -= hiroAT
    print("hiroが",hiro.attribute,"属性で",hiroAT,"の攻撃")
    print("enemyの残り体力は",enemy_hp)
    # 敵の後攻
    hiro_hp -= enemyAT
    print("enemyが",enemy.attribute,"属性で",enemyAT,"の攻撃")
    print("hiroの残り体力は",hiro_hp)

if hiro_hp > 0:
    print("hiroの勝ち")
else:
    print("enemyの勝ち")