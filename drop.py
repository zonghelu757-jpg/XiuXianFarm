
import random 
def monster_drop(player):
    chance =random .randint(1, 100)
    if chance <= 10:
        player .iron_sword += 1
        print("获得掉落： 铁剑")
    else:
        print("没有获得装备")
        