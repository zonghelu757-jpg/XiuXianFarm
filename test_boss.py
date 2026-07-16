from player import Player
from boss import create_wolf_king
from fight import fight


player = Player()

boss = create_wolf_king()

fight(player, boss)