import unittest

from game.LogikaGry import LogikaGry
from game.Wiadomosci import Wiadomosci


class MainTesting(unittest.TestCase):
    def test1_bad_numbers(self):
        game = LogikaGry()

        rn = 1
        while rn in game.secret_key:
            rn += 1

        print(f"KOD: {game.secret_key}")
        self.assertEqual(game.check_turn([rn, rn, rn, rn]), (0, 0))

    def test3_2_bad_pos_2_hit(self):
        game = LogikaGry()
        test = []

        while game.secret_key[2] == game.secret_key[3]:
            game.setup_game()

        test = list(game.secret_key)

        temp = test[3]
        test[3] = test[2]
        test[2] = temp

        print(f"KOD: {game.secret_key}")
        print(f"Input: {test}")
        self.assertEqual(game.check_turn(test), (2, 2))

    def test4_4_hit(self):
        with self.assertLogs(level='INFO') as log:
            game = LogikaGry()

            test = game.secret_key
            print(f"KOD: {game.secret_key}")
            self.assertEqual(game.check_turn(test), (4, 0))
            self.assertIn(Wiadomosci.MSG_END_GAME_WIN, log.output[0])

    def test5_12_incorrect_end_game(self):
        with self.assertLogs(level='INFO') as log:
            game = LogikaGry()
            test = game.secret_key.copy()
            test.reverse()

            for _ in range(12):
                game.interact(test)

            self.assertIn(Wiadomosci.MSG_END_GAME_LOSE, log.output[0])

    def test6_bad_input(self):
        game = LogikaGry()
        start = game.current_round

        game.interact("test")
        game.interact("111")
        game.interact("11111")
        game.interact("0000")

        self.assertEqual(game.current_round, start)


if __name__ == '__main__':
    unittest.main()
