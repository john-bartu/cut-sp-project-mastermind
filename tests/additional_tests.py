import unittest

from game.cheat_logic import CheatGameLogic
from game.logic import GameLogic


class AdditionalTests(unittest.TestCase):
    def test_2_bad_pos_2_hit_hacked(self):
        game = CheatGameLogic()
        test = []

        while game.secret_code[2] == game.secret_code[3]:
            game.setup_game()

        test = list(game.secret_code)

        temp = test[3]
        test[3] = test[2]
        test[2] = temp

        print(f"KOD: {game.secret_code}")
        print(f"Input: {test}")
        self.assertEqual(game.interact(test), (0, 0))

    def test_2_bad_pos_2_hit_hacked(self):

        tests = [
            [[1, 1, 1, 1], [1, 1, 1, 1], (4, 0)],
            [[1, 1, 1, 1], [1, 1, 1, 2], (3, 0)],
            [[1, 1, 1, 1], [2, 2, 2, 1], (1, 0)],
            [[1, 1, 1, 1], [2, 2, 1, 2], (1, 0)],
            [[2, 2, 1, 1], [1, 1, 2, 2], (0, 4)],
            [[1, 2, 1, 2], [1, 2, 2, 1], (2, 2)],
            [[1, 2, 2, 4], [2, 2, 4, 1], (1, 3)],
            [[1, 1, 2, 2], [2, 2, 2, 3], (1, 1)]
        ]

        game = GameLogic()

        for example in tests:
            game.secret_code = example[0]
            print(f"KOD: {game.secret_code}")
            print(f"Input: {example[1]}")
            self.assertEqual(game.interact(example[1]), example[2])


if __name__ == '__main__':
    unittest.main()
