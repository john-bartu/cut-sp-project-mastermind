from game.rules import GameRules


class CheatGameRules(GameRules):

    def check(self, input_code: list, secret_code: list):
        """
Cheated return result always zeros
        :param input_code: list of digits
        :param secret_code: correct list of digits
        :return: Tuple (DigitsInCorrectPlace,OtherCorrectDigits)
        """
        return 0, 0
