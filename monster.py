import random
class Monster:
    def __init__(self, name, hp, attack, gold, exp, drop):
        self .name = name
        self .hp = hp
        self .attack = attack
        self . gold = gold
        self . exp = exp
        self . drop = drop
#========================
#怪物数据
#========================
MONSTERS = {"野狼": {"hp": 30, "attack": 5, "gold": 20, "exp": 20, "drop": "狼牙"}, "野猪": {"hp": 45, "attack": 8, "gold": 30, "exp": 30, "drop": "野猪肉"},"妖狐": {"hp": 50, "attack": 8, "gold": 40, "exp": 20, "drop": "狐皮"}, "巨蛇": {"hp": 80, "attack": 12, "gold": 80, "exp": 40, "drop": "蛇肉"}, "黑熊":{"hp": 120, "attack": 15, "gold": 150, "exp": 80, "drop": "熊掌"}}

# ==============
# 创造指定怪物
# ==============

def create_monster(name):
    data = MONSTERS[name]

    return Monster(name, data["hp"], data["attack"], data["gold"], data["exp"], data["drop"])
# ==============
# 随机怪物
# ==============
def random_monster():
    name = random . choice(list(MONSTERS . keys()))
    return create_monster(name)
