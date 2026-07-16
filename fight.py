from drop import monster_drop
from level import check_level_up

def fight(player , monster):
    print(f"\n 你遇到了{monster .name}")
    while monster . hp > 0 and player . hp > 0:
        print(f"{monster .name} 剩余生命： {monster .hp}")
        input("按回车攻击")
        monster . hp -= player . attack
        print(f"你造成{player .attack} 点伤害")

        if monster . hp > 0:
            print(f"{monster . name} 攻击了你！")
            print(f"你受到{monster . attack} 点伤害")
            print(f"你的生命{player .hp}")
        else:
            break

        if player .hp <= 0:
            print("你被野狼击败了！")
        else:
            print(f"{player . weapon}砍向了{monster . name}")
    player . gold += monster . gold
    player . exp += monster . exp
    check_level_up(player)

    drop = monster . drop
    if drop not in player . items:
        player .items[drop] = 0
    player . items[drop] += 1        
    print(f"获得掉落: {monster .drop}")
    

    print(f"获得金币 +{monster . gold}") 
    monster_drop(player)
    print(f"当前金币 {player . gold}")
    print(f"获得经验 +{monster .exp}")
            
        