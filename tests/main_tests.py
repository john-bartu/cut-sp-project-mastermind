import unittest

from game.logic import GameLogic
from game.messages import Messages


def repeat(times):
    def repeatHelper(f):
        def callHelper(*args):
            for i in range(0, times):
                f(*args)

        return callHelper

    return repeatHelper


def is_each_digit_occurs_only_once(secret_code):
    for digit in secret_code:
        if secret_code.count(digit) > 1:
            return False
    return True


class MainTests(unittest.TestCase):
    @repeat(100)
    def test1_bad_numbers(self):
        game = GameLogic()

        rn = 1
        while rn in game.secret_code:
            rn += 1

        print(f"SECRET_CODE: {game.secret_code}")
        print(f"Input: {[rn, rn, rn, rn]}")
        self.assertEqual(game.interact([rn, rn, rn, rn]), (0, 0))

    @repeat(100)
    def test2_bad_places(self):
        game = GameLogic()

        while not is_each_digit_occurs_only_once(game.secret_code):
            game.generate_new_secret_key()

        print(f"SECRET_CODE: {game.secret_code}")

        test_code = game.secret_code.copy()
        test_code.reverse()

        print(f"Input: {test_code}")
        self.assertEqual(game.interact(test_code), (0, 4))

    @repeat(100)
    def test3_2_bad_pos_2_hit(self):
        game = GameLogic()

        while game.secret_code[2] == game.secret_code[3]:
            game.setup_game()

        test = list(game.secret_code)

        temp = test[3]
        test[3] = test[2]
        test[2] = temp

        print(f"SECRET_CODE: {game.secret_code}")
        print(f"Input: {test}")
        self.assertEqual(game.interact(test), (2, 2))

    @repeat(100)
    def test4_4_hit(self):
        with self.assertLogs(level='INFO') as log:
            game = GameLogic()

            test = game.secret_code
            print(f"SECRET_CODE: {game.secret_code}")
            self.assertEqual(game.interact(test), (4, 0))
            self.assertIn(Messages.MSG_END_GAME_WIN, log.output[0])

    @repeat(100)
    def test5_12_incorrect_end_game(self):
        with self.assertLogs(level='INFO') as log:
            game = GameLogic()
            test = game.secret_code.copy()
            test.reverse()

            for _ in range(12):
                game.interact(test)

            self.assertIn(Messages.MSG_END_GAME_LOSE, log.output[0])

    @repeat(100)
    def test6_bad_input(self):
        game = GameLogic()
        start = game.current_round

        game.interact("test")
        game.interact("111")
        game.interact("11111")
        game.interact("0000")
        game.interact("7777")

        self.assertEqual(game.current_round, start)


if __name__ == '__main__':
    unittest.main()
