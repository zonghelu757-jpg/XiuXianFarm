def check_realm(player):
    if player .exp >= 100 and player .realm == "练气":
        player . realm = "筑基"
        player . attack += 20
        player . hp += 50
        print()
        print("恭喜突破筑基！")
