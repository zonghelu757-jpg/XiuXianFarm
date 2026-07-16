def check_level_up(player):

    while player .exp >= 100:
        player .exp -= 100 
        if player . realm == "练气":
            player . realm = "练气二层"

            player . max_hp += 20
            player . hp = player . max_hp
            player . attack += 5

            print()
            print("======")
            print("突破成功！")
            print("境界提升：练气二层")
            print("生命 + 20")
            print("攻击 + 5")
            print("======")