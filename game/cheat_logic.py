from game.cheat_rules import CheatGameRules
from game.logic import GameLogic


class CheatGameLogic(GameLogic, CheatGameRules):
    """ Implements GameLogic with override cheated game rules"""
    pass
