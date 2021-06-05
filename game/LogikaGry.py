import random

from game.RegulyGry import RegulyGry


class LogikaGry(RegulyGry):
    history_game = []
    history_result = []
    secret_key = ()
    current_round = 0

    def __init__(self):
        self.setup_game()

    def generate_new_secret_key(self):
        self.secret_key = [random.randint(1, 6) for _ in range(4)]

    def reset_round_count(self):
        self.current_round = 0

    def setup_game(self):
        self.generate_new_secret_key()
        self.reset_round_count()
        self.history_game.clear()
        self.history_result.clear()

    def interact(self, user_raw_input):
        user_input = []
        # parse text to numbers
        for character in user_raw_input:
            try:
                number = int(character)

                if number - 1 in range(6):
                    user_input.append(number)
                else:
                    raise ValueError("Wpisana liczba jest spoza zakresu 1-6: " + character)

            except ValueError:
                raise ValueError("Wpisane dane wejściowe nie są cyfrą: " + character)

        if len(user_input) < 4:
            raise ValueError("Zbyt mała ilość cyfr")

        if len(user_input) > 4:
            raise ValueError("Zbyt duża ilość cyfr")

        result = self.check(user_input, self.secret_key)

        if result[0] == 4:
            self.GraWygrana()

        self.history_result.append(result)
        self.history_game.append(user_input)
        self.current_round += 1

        if self.current_round == 12:
            self.GraPrzegrana()

    def GraWygrana(self):
        print(f"Wygrana!")
        self.setup_game()

    def GraPrzegrana(self):
        print(f"Przekroczone liczbę kroków")
        self.setup_game()
