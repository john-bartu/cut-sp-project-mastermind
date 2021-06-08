import unittest

from game.logic import GameLogic
from game.cheat_logic import CheatGameLogic


class AdditionalTests(unittest.TestCase):
    def test_2_bad_pos_2_hit_hacked(self):
        game = CheatGameLogic()
        test = []

        while game.additional_tests[2] == game.additional_tests[3]:
            game.setup_game()

        test = list(game.additional_tests)

        temp = test[3]
        test[3] = test[2]
        test[2] = temp

        print(f"KOD: {game.additional_tests}")
        print(f"Input: {test}")
        self.assertEqual(game.check_turn(test), (0, 0))


if __name__ == '__main__':
    unittest.main()
