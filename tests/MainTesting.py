import unittest

from game.LogikaGry import LogikaGry


class MainTesting(unittest.TestCase):
    def test_bad_numbers(self):
        game = LogikaGry()

        rn = 1
        while rn in game.secret_key:
            rn += 1

        print(f"KOD: {game.secret_key}")
        self.assertEqual(game.check_turn([rn, rn, rn, rn]), (0, 0))

    def test_2_bad_pos_2_hit(self):
        game = LogikaGry()

        test = game.secret_key

        temp = test[3]
        test[3] = test[2]
        test[3] = temp

        print(f"KOD: {game.secret_key}")
        self.assertEqual(game.check_turn(test), (2, 2))

    def test_4_hit(self):
        game = LogikaGry()

        test = game.secret_key
        print(f"KOD: {game.secret_key}")
        self.assertEqual(game.check_turn(test), (4, 0))

    def test_bad_input(self):
        game = LogikaGry()
        start = game.current_round

        game.interact("test")
        game.interact("111")
        game.interact("11111")
        game.interact("0000")

        self.assertEqual(game.current_round, start)


if __name__ == '__main__':
    unittest.main()
