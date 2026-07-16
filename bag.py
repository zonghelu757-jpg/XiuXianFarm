
def show_bag(player):
    
    print("======角色状态======")
    print(f"金币:", player . gold)
    print(f"经验:", player . exp)
    print(f"生命:", player . hp)
    print(f"境界: {player . realm}" )
    print(f"当前武器: {player . weapon}")
    print(f"攻击力： {player . attack}")
    
    print()
    print("======物品背包======")

    print(f"聚灵草 x", player . grass)
    print(f"灵鸡 x", player . chicken)
    print(f"灵兔 x", player . rabbit)
    
    print(f"回血丹 x", player . potion)
    print(f"木剑 x", player . wood_sword)
    print(f"铁剑 x", player . iron_sword)
    if len(player . items) == 0:
        print("背包为空")
    else:
        for item, count in player . items . items():
            print(f"{item}: {count}")
    
    
    input("\n按回车返回...")
    
    while True :
        print("1. 装备木剑")
        print("2. 装备铁剑")
        print("0. 返回地图")

        choice = input("选择：")
        if choice == "1":
            player .weapon ="木剑"
            player . update_attack()
            print(f"你已装备{player . weapon}")
        elif choice == "2":
            player . weapon = "铁剑"
            player . update_attack()
            print(f"你已装备{player .weapon}")
               
        elif choice == "0":
            break 
         
    