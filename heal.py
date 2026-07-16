def use_grass(player):

    if player .grass <= 0:
        print("没有灵草！")
        return
    if player .hp >= 100:
        print("生命已满! ")
        return
    player . grass -= 1

    player . hp += 20

    if player . hp > 100:
        player . hp = 100

    print("使用一株灵草！")
    print(f"生命恢复到： {player .hp}")