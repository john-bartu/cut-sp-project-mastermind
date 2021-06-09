import random

from game.cheat_logic import CheatGameLogic
from game.logic import GameLogic


class GameController:
    CHEAT_CHANCE = 0.1
    game_logic = None

    def __init__(self):
        random_number = random.random()

        if random_number > self.CHEAT_CHANCE:
            self.game_logic = GameLogic()
        else:
            self.game_logic = CheatGameLogic()

    def check_if_cheating(self):
        """
Checks if game_logic is instance of CheatGameLogic rather than GameLogic
        :return: true if game_logic is instance of CheatGameLogic
        """
        return isinstance(self.game_logic, CheatGameLogic)
