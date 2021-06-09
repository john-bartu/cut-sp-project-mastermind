import logging
import random

from game.exceptions import InputNotCertainTypeError, DigitNotInRangeError, CodeLengthNotEqualError, InputError
from game.messages import Messages
from game.rules import GameRules
from game.states import GameState


class GameLogic(GameRules):
    game_state = GameState.INCOMPLETE
    history_game = []
    history_result = []
    secret_code = ()
    current_round = 0

    def __init__(self):
        log_formatter = logging.Formatter("%(levelname)-5s]  %(message)s")
        root_logger = logging.getLogger()
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)
        self.setup_game()

    def generate_new_secret_key(self):
        self.secret_code = [random.randint(self.MINIMAL_NUMBER, self.MAXIMAL_NUMBER) for _ in
                            range(self.CODE_LENGTH)]

    def reset_round_count(self):
        self.current_round = 0

    def setup_game(self):
        self.generate_new_secret_key()
        self.reset_round_count()
        self.history_game.clear()
        self.history_result.clear()
        self.current_round = 0
        self.game_state = GameState.INCOMPLETE
        logging.info(self.secret_code)

    def parse_input(self, user_raw_input):
        user_input = []
        # parse text to numbers
        for character in user_raw_input:
            try:
                number = int(character)

                if number - self.MINIMAL_NUMBER in range(self.MAXIMAL_NUMBER - self.MINIMAL_NUMBER + 1):
                    user_input.append(number)
                else:
                    raise DigitNotInRangeError(number, self.MINIMAL_NUMBER, self.MAXIMAL_NUMBER)

            except ValueError:
                raise InputNotCertainTypeError(character)

        if len(user_input) != self.CODE_LENGTH:
            raise CodeLengthNotEqualError(len(user_input), self.CODE_LENGTH)

        return user_input

    def check_turn(self, user_input):
        result = self.check(user_input, self.secret_code)

        if result[0] == self.CODE_LENGTH:
            self.game_state = GameState.WON
            logging.info(Messages.MSG_END_GAME_WIN)

        self.history_result.append(result)
        self.history_game.append(user_input)

        self.current_round += 1

        if self.current_round == self.NUMBER_OF_TRIES:
            self.game_state = GameState.LOST
            logging.info(Messages.MSG_END_GAME_LOSE)

        return result

    def interact(self, user_raw_input):
        try:
            user_input = self.parse_input(user_raw_input)
            return self.check_turn(user_input)
        except InputError:
            return 0, 0

    def get_game_state(self):
        return self.game_state
