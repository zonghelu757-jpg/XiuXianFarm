from monster import Monster

def create_wolf_king():

    return Monster("狼王", 300, 20, 300, 100, "狼王之牙")

def boss_reward(player):

    if "狼王之牙" not in player.items:
        player.items["狼王之牙"] = 0

    player.items["狼王之牙"] += 1

    print("获得狼王之牙 X1")