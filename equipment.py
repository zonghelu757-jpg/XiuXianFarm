EQUIPMENTS = {"木剑":{"attack": 15, "quality": "普通", "price": 0}, "铁剑": {"attack": 20, "quality": "普通", "price": 100}, "青云剑":{"attack": 70, "quality":"优秀", "price": 600}}
def equip_weapon(player):
    print()
    print("======装备======")
    print("1. 木剑")
    print("2. 铁剑")
    print("3. 青云剑")
    print("0. 返回 ")
    choice = input("选择: ")
    if choice == "1":
        player . weapon = "木剑"
        player . update_attack()

        print("装备木剑")
    elif choice == "2":
        if player . iron_sword >0:
            player . weapon = "铁剑"
            player . update_attack()
            print("装备铁剑")
        else:
            print("没有铁剑")
    elif choice == "3":

        if player.qingyun_sword > 0:

         player.weapon = "青云剑"
         player.update_attack()
         print("装备青云剑")

        else:

            print("没有青云剑")
    elif choice == "0":
        return