class InputError(Exception):
    pass


class CodeLengthNotEqualError(InputError):
    def __init__(self, input_code_length, code_length=4):
        """
Exception raised for errors in the input code_digit.
        :param input_code_length: input code_digit which caused the error
        :param code_length:  code length
        """
        self.input_code_length = input_code_length
        self.message = f"Code length is not equal {code_length}"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.input_code_length} -> {self.message}'


class InputNotCertainTypeError(InputError):
    def __init__(self, code_digit):
        """
Exception raised for errors in the input code_digit.
        :param code_digit: input code_digit which caused the error
        """
        self.code_digit = code_digit
        self.message = f"Input is not digit {code_digit}"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.code_digit} -> {self.message}'


class DigitNotInRangeError(InputError):
    def __init__(self, code_digit, min_length=1, max_length=6):
        """
Exception raised for errors in the input code_digit.
        :param code_digit: input code_digit which caused the error
        :param min_length: minimal code length
        :param max_length: maximal code length
        """
        self.code_digit = code_digit
        self.message = f"Code digit is not in ({min_length}, {max_length}) range"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.code_digit} -> {self.message}'
