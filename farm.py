import random
def plant(player):
    if player .gold >= 10:
        player .gold -= 10
        gain = random.randint(1 , 3)
        player . grass += gain
        player . exp += gain * 5
        print("获得", gain, "株聚灵草")
    else:
        print("金币不足")
def sell(player):
    if player .grass >0:
        money = player . grass * 20
        player . gold += money
        print("获得", money, "金币") 
        player . grass = 0
    else:
        print("没有灵草")