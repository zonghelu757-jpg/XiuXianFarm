
from item import ITEMS
def shop(player):
    while True:

        print("======商店======")
        print("1. 购买物品")
        print("2. 出售物品")
        print("0. 返回")
        
        choice = input("选择:")

        if choice == "1":
            buy_menu(player)
        
        elif choice == "2":
            sell_menu(player)
        elif choice == "0":
            break
        else:
            print("输入错误")

# =======================
# 购买系统 
# =======================
def buy_menu(player):
    while True:
        print()
        print("======购买======")
        buy_list = []
        for item, data in ITEMS.items():
            if "buy" in data:
                buy_list .append(item)
        for i, item in enumerate(buy_list, 1):
                    
            print(f"{i} . {item} 价格:{ITEMS[item] ['buy']}")
            print("0. 返回")
                    
            choice = input("选择购买:")
                    
            if choice == "0":
                break
            if choice. isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(buy_list):
                        item = buy_list[choice-1]
                        buy_item(player , item)
                    else:
                        print("没有这个选项")
            else:
                print("请输入数字")

def buy_item(player, item):
    price = ITEMS[item] ["buy"]

    if player . gold < price:
        print("金币不足")
        return

    player . gold -= price
    if item not in player . items:
        player .items[item] = 0
    player .items[item] += 1
    print(f"购买成功： {item}")

# ===========================
# 出售系统
# ===========================
def sell_menu(player):
    while True:
        print()
        print("======出售======")

        sell_list = []
        for item, count in player . items . items():
            if count > 0:
                sell_list .append(item)

        if len(sell_list) == 0:
            print("没有可以出售的东西")
            break
        for i, item in enumerate(sell_list, 1):
            print(f"{i}. {item} 数量:{player . items[item]}")
        print("0. 返回")
        choice=input("选择出售: ")

        if choice == "0":
                break

        if choice .isdigit():
            choice =int(choice)

            if 1 <= choice <= len(sell_list):
                item=sell_list[choice-1]
                sell_item(player .item)
            else:
                print("没有这个选项")
        else:
            print("请输入数字")

def sell_item(player , item):
    if ITEMS[item] ["type"] != "材料":
        print("这个物品不能出售")
        return
    
    amount =input("出售数量(all全部): ")
    if amount .lower() == "all":
        amount = player . items[item]

    else:
        try:
            amount =int(amount)
        except:
            print("请输入数字")
            return
        
    if amount <= 0 or amount > player . items[item]:
        print("数量错误")
        return
    
    price = ITEMS[item]["sell"]

    total = price * amount
    player . gold += total
    player . items[item] -= amount

    if player . items[item]==0:
        del player .items[item]
    print(f"出售 {item} * {amount}")
    print(f"获得金币 +{total}")

    








