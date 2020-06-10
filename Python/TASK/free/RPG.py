import random

# 主人公と敵の体力を入力
hiro_hp = 120
enemy_hp = 150

print("戦闘開始")

# 先行を主人公とする
# 以下から、戦闘を開始。どちらかのhpの値が0になるまで実行
while (hiro_hp > 0 or enemy_hp > 0):

    # 属性の設定
    attribute = ["火","水","雷"]
    # 主人公の属性
    h = random.randint(0,2)
    attributeH = attribute[h]
    # 敵の属性
    e = random.randint(0,2)
    attributeE = attribute[e]

    # 主人公と敵の攻撃力
    attack_hiro = random.randint(20,40)
    attack_enemy = random.randint(10,15)

    # # hiroの攻撃値が0.5倍になるケースをまとめる
    # if (attributeH == "火" and attributeE == "水") or (attributeH == "水" and attributeE == "雷") or (attributeH == "雷" and attributeE == "火"):
    #     (attack_hiro == attack_hiro * 0.5) and (attack_enemy == attack_enemy * 1.5)
    # #hiroの攻撃値が1.5倍になるケースをまとめる
    # elif (attributeH == "水" and attributeE == "火") or (attributeH == "雷" and attributeE == "水") or (attributeH == "火" and attributeE == "雷"):
    #     (attack_hiro == attack_hiro * 1.5) and (attack_enemy == attack_enemy * 0.5)
    # # 等倍分
    # else:
    #     (attack_hiro == attack_hiro * 1.0) and (attack_enemy == attack_enemy * 1.0)
    

    # 主人公を先行
    enemy_hp -= attack_hiro
    print("hiroが",attributeH,"属性で",attack_hiro,"の攻撃")
    print("enemyの残り体力は",enemy_hp)
    # 敵の後攻
    hiro_hp -= attack_enemy
    print("enemyが",attributeE,"属性で",attack_enemy,"の攻撃")
    print("hiroの残り体力は",hiro_hp)

if hiro_hp > 0:
    print("hiroの勝ち")
else:
    print("enemyの勝ち")