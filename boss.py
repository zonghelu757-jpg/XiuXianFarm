from monster import Monster

def create_wolf_king():

    return Monster("狼王", 300, 20, 300, 100, "狼王之牙")

def boss_reward(player, boss):

    item = boss.drop

    if item not in player.items:
        player.items[item] = 0

    player.items[item] += 1

    print(f"获得{item} x1")