import random

from game.cheat_logic import CheatGameLogic
from game.logic import GameLogic


class GameController:
    HACKED_CHANGE = 0.1
    game_logic = None

    def __init__(self):
        random_number = random.random()

        if random_number > self.HACKED_CHANGE:
            self.game_logic = GameLogic()
        else:
            self.game_logic = CheatGameLogic()
