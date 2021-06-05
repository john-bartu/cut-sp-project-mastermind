from game.RegulyGry import RegulyGry


class FalszyweRegulyGry(RegulyGry):
    def check(self, input_code: list, secret_code: list):
        return 0, 0
