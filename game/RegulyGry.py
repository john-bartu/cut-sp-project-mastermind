class RegulyGry:
    def check(self, input_code: list, secret_code: list):
        count_good_position = 0
        count_good_number = 0

        checked_count = {i + 1: 0 for i in range(6)}

        for number_index in range(len(input_code)):

            value = input_code[number_index]

            # is in secret code
            if secret_code.count(value) - checked_count[value] > 0:

                # is on correct place in secret code
                if input_code[number_index] == secret_code[number_index]:
                    count_good_position += 1
                else:
                    count_good_number += 1

                checked_count[value] += 1

        return count_good_position, count_good_number
