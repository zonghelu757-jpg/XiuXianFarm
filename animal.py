def animal_income(player):
    player . gold += player . chicken * 5
    player . spirit_stone += player . rabbit
def buy_chicken(player):
    if player .gold >= 100:
        player .gold -= 100
        player .chicken += 1
        print("购买成功灵鸡")
    else:
        print("金币不足")
def buy_rabbit(player):
    if player . gold >= 200:
        player . gold-= 200
        player . rabbit += 1
        print("成功购买灵兔")
    else:
        print("金币不足")