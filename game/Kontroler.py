import random

from game.LogikaGry import LogikaGry, FalszywaLogikaGry


class Kontroler:
    HACKED_CHANGE = 0.1
    game_logic = None

    def __init__(self):
        random_number = random.random()

        if random_number > self.HACKED_CHANGE:
            self.game_logic = LogikaGry()
        else:
            self.game_logic = FalszywaLogikaGry()
