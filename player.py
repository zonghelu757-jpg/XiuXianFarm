from equipment import EQUIPMENTS
class Player:
    def __init__(self):
        self .gold = 100
        self .spirit_stone = 0
        self . exp = 0
        self . realm = "练气"
        self . grass = 0
        self . chicken = 0
        self . rabbit = 0
        self . max_hp = 100
        self .attack = 10
        self . potion = 3
        self . wood_sword = 1
        self . iron_sword = 0
        self . weapon = "木剑"
        self . qingyun_sword = 0
        self . items = {}
        
    def update_attack(self):

        self .attack =EQUIPMENTS[self .weapon] ["attack"]
        