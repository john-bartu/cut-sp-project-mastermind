import logging
import random

from game.FalszyweRegulyGry import FalszyweRegulyGry
from game.RegulyGry import RegulyGry
from game.Wiadomosci import Wiadomosci


class LogikaGry(RegulyGry):
    history_game = []
    history_result = []
    secret_key = ()
    current_round = 0

    def __init__(self):
        self.setup_game()
        log_formatter = logging.Formatter("%(levelname)-5s]  %(message)s")
        root_logger = logging.getLogger()
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)

    def generate_new_secret_key(self):
        self.secret_key = [random.randint(self.MINIMAL_NUMBER, self.MAXIMAL_NUMBER) for _ in
                           range(self.CODE_LENGTH)]

    def reset_round_count(self):
        self.current_round = 0

    def setup_game(self):
        self.generate_new_secret_key()
        self.reset_round_count()
        self.history_game.clear()
        self.history_result.clear()

    def parse_input(self, user_raw_input):
        user_input = []
        # parse text to numbers
        for character in user_raw_input:
            try:
                number = int(character)

                if number - self.MINIMAL_NUMBER in range(self.MAXIMAL_NUMBER - self.MINIMAL_NUMBER + 1):
                    user_input.append(number)
                else:
                    raise ValueError(
                        f"Wpisana liczba jest spoza zakresu {self.MINIMAL_NUMBER}-{self.MAXIMAL_NUMBER}: " + character)

            except ValueError:
                raise ValueError("Wpisane dane wejściowe nie są cyfrą: " + character)

        if len(user_input) < self.CODE_LENGTH:
            raise ValueError("Zbyt mała ilość cyfr")

        if len(user_input) > self.CODE_LENGTH:
            raise ValueError("Zbyt duża ilość cyfr")

        return user_input

    def check_turn(self, user_input):
        result = self.check(user_input, self.secret_key)

        if result[0] == self.CODE_LENGTH:
            self.game_won()

        self.history_result.append(result)
        self.history_game.append(user_input)

        self.current_round += 1

        if self.current_round == self.NUMBER_OF_TRIES:
            self.game_lost()

        return result

    def interact(self, user_raw_input):
        try:
            user_input = self.parse_input(user_raw_input)
            return self.check_turn(user_input)
        except ValueError:
            return 0, 0

    def game_won(self):
        logging.info(Wiadomosci.MSG_END_GAME_WIN)
        self.setup_game()

    def game_lost(self):
        logging.info(Wiadomosci.MSG_END_GAME_LOSE)
        self.setup_game()


class FalszywaLogikaGry(LogikaGry, FalszyweRegulyGry):
    pass
