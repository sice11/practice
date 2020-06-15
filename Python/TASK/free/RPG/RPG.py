import random

# 主人公と敵の体力を入力
hiro_hp = 120.0
enemy_hp = 150.0

print("戦闘開始")

# 先行を主人公とする
# 以下から、戦闘を開始。どちらかのhpの値が0になるまで実行
while (hiro_hp > 0 and enemy_hp > 0):

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

    # 主人公と敵の属性による倍率変動を変数に
    # 倍率が半減する場合
    attack_hiro_05 = attack_hiro * 0.5
    attack_enemy_05 = attack_enemy * 0.5
    # 倍率が1.5倍になる場合
    attack_hiro_15 = attack_hiro * 1.5
    attack_enemy_15 = attack_enemy * 1.5
    # 倍率が等倍の場合
    attack_hiro_1 = attack_hiro * 1.0
    attack_enemy_1 = attack_enemy * 1.0

    # hiroの攻撃値が0.5倍になるケースをまとめる
    if (attributeH == "火" and attributeE == "水") or (attributeH == "水" and attributeE == "雷") or (attributeH == "雷" and attributeE == "火"):
        (attack_hiro_05) and (attack_enemy_15)
    #hiroの攻撃値が1.5倍になるケースをまとめる
    elif (attributeH == "水" and attributeE == "火") or (attributeH == "雷" and attributeE == "水") or (attributeH == "火" and attributeE == "雷"):
        (attack_hiro_15) and (attack_enemy_05)
    # 等倍分
    else:
        (attack_hiro_1) and (attack_enemy_1)
    

    #以下に表示される攻撃値は、属性値を反映しない値
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