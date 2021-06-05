import unittest

from game.LogikaGry import LogikaGry, FalszywaLogikaGry


class AdditionalTesting(unittest.TestCase):
    def test_2_bad_pos_2_hit_hacked(self):
        game = FalszywaLogikaGry()
        test = []

        while game.secret_key[2] == game.secret_key[3]:
            game.setup_game()

        test = list(game.secret_key)

        temp = test[3]
        test[3] = test[2]
        test[2] = temp

        print(f"KOD: {game.secret_key}")
        print(f"Input: {test}")
        self.assertEqual(game.check_turn(test), (0, 0))


if __name__ == '__main__':
    unittest.main()
