from map import show_map
from player import Player
from save import load_game

player = Player()

load_game(player)

show_map(player)