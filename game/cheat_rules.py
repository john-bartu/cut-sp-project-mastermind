from game.rules import GameRules


class CheatGameRules(GameRules):
    def check(self, input_code: list, secret_code: list):
        return 0, 0
