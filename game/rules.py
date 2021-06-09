class GameRules:
    MINIMAL_NUMBER = 1
    MAXIMAL_NUMBER = 6
    NUMBER_OF_TRIES = 12
    CODE_LENGTH = 4

    def check(self, input_code: list, secret_code: list):
        """
Checks if given code is equal secret code and generates return (DigitsInCorrectPlace,OtherCorrectDigits)
        :param input_code: list of digits
        :param secret_code: correct list of digits
        :return: Tuple (DigitsInCorrectPlace,OtherCorrectDigits)
        """
        count_good_position = 0
        count_good_number = 0

        dummy_input = input_code.copy()
        dummy_passcode = secret_code.copy()

        dummy_input2 = []
        dummy_passcode2 = []

        # Check if digit in right position
        for index in range(len(dummy_input)):
            if dummy_input[index] == dummy_passcode[index]:
                count_good_position += 1
            else:
                dummy_input2.append(dummy_input[index])
                dummy_passcode2.append(dummy_passcode[index])

        # Check other digits if exists in code
        for number in dummy_input2:
            if number in dummy_passcode2:
                count_good_number += 1
                dummy_passcode2.remove(number)

        return count_good_position, count_good_number

    def check_not_so_easy(self, input_code: list, secret_code: list):
        count_good_position = 0
        count_good_number = 0

        for number_index in range(len(input_code)):
            if input_code[number_index] == secret_code[number_index]:
                count_good_position += 1
            if input_code[number_index] != secret_code[number_index] and input_code[number_index] in secret_code:
                count_good_number += 1

        return count_good_position, count_good_number
