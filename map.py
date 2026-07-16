from monster import random_monster 
from boss import create_wolf_king
from fight import fight
from bag import show_bag
from shop import shop
from quest import village_quest
from equipment import equip_weapon
from save import save_game

from status import show_status

import random
def show_map(player):

    print(f"金币: {player .gold}")
    print(f"生命: {player . hp}")
    print(f"灵草: {player .grass}")

    while True:

        print("\n ==== 世界地图 ====")
        print("1. 灵田")
        print("2. 森林")
        print("3. 村庄")
        print("4. 村长")
        print("5. 狼王洞穴")
        print("6. 使用灵草回血")
        print("7. 背包")
        print("8. 查看角色")
        print("9.保存游戏")
        print("0 返回")

        choice = input("选择：")

        if choice =="1":
            enter_farm(player)
        elif choice == "2":
            enter_forest(player)
        elif choice == "3":
            enter_village(player)
        elif choice == "4":
            village_quest(player)
        elif choice == "5":
            enter_boss(player)
        elif choice == "6":
            from heal import use_grass
            use_grass(player)
        elif choice == "7":
            show_bag(player)
        elif choice == "8":
            show_status(player)
        elif choice == "9":
            save_game(player)
        elif choice == "0":
            break

def enter_farm(player):
    print("\n 灵田收获中...")
    gain = random .randint(1, 3)
    player .grass += gain
    print(f"获得灵草 +{gain}")

def enter_shop(player):
    shop(player)

def enter_boss(player):

    print("\n进入狼王洞穴...")

    boss = create_wolf_king()

    print(f"你遇到了{boss.name}")

    fight(player,boss)

def enter_forest(player):
    print("\n 进入妖兽森林...")

    event = random .randint(1, 100)
    if event <= 60:
       monster = random_monster() 
       print(f"遇到{monster .name}!")
       
       fight(player , monster)
    elif event <= 75:
        player .gold += 10
        print("捡到金币 +10")
    elif event <=90:
        print("发现灵草 +1")
        player . grass += 1
    else:
        print("什么都没有发生")

def enter_village(player):
    while True:
        print()
        print("======村庄======")
        print("1. 商店")
        print("2. 村长")
        print("3. 装备")
        print("4. 背包")
        print("0. 返回")
        
        choice = input("选择: ")
        if choice == "1":
            shop(player)

        elif choice == "2":
            village_quest(player)
        elif choice == "3":
            equip_weapon(player)
        elif choice == "4":
            show_bag(player)
        elif choice == "0":
            break
        else:
            print("输入错误！")