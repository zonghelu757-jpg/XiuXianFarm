from player import Player
from boss import create_wolf_king
from fight import fight


player = Player()
player.attack =100

boss = create_wolf_king()

fight(player, boss)

print("最终背包:")
print(player.items)