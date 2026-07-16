import json


def save_game(player):

    data = {

        "gold": player.gold,
        "spirit_stone": player.spirit_stone,

        "exp": player.exp,
        "realm": player.realm,

        "grass": player.grass,

        "hp": player.hp,

        "max_hp": player.max_hp,

        "attack": player.attack,

        "weapon": player.weapon,

        "iron_sword": player.iron_sword,

        "items": player . items
    }


    with open("save.json","w",encoding="utf-8") as f:

        json.dump(data,f,ensure_ascii=False,indent=4)


    print("保存成功！")



def load_game(player):

    try:

        with open("save.json","r",encoding="utf-8") as f:

            data=json.load(f)


        player.gold=data["gold"]
        player.spirit_stone=data["spirit_stone"]

        player.exp=data["exp"]
        player.realm=data["realm"]

        player.grass=data["grass"]

        player.hp=data.get("hp", 100)

        player.max_hp=data["max_hp"]

        player.attack=data["attack"]

        player.weapon=data["weapon"]

        player.iron_sword=data["iron_sword"]

        player.items =data["items"]


        print("读取存档成功！")


    except FileNotFoundError:

        print("没有存档，开始新游戏")