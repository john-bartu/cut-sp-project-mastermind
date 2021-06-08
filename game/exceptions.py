class InputError(Exception):
    pass


class CodeLengthNotEqualError(InputError):
    """Exception raised for errors in the input code_digit.

    Attributes:
        code_digit -- input code_digit which caused the error
        code_length -- code length
    """

    def __init__(self, input_code_length, code_length=4):
        self.input_code_length = input_code_length
        self.message = f"Code length is not equal {code_length}"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.input_code_length} -> {self.message}'


class InputNotCertainTypeError(InputError):
    """Exception raised for errors in the input code_digit.

    Attributes:
        code_digit -- input code_digit which caused the error
    """

    def __init__(self, code_digit):
        self.code_digit = code_digit
        self.message = f"Input is not digit {code_digit}"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.code_digit} -> {self.message}'


class DigitNotInRangeError(InputError):
    """Exception raised for errors in the input code_digit.

    Attributes:
        code_digit -- input code_digit which caused the error
        min_length -- minimal code length
        max_length -- maximal code length
    """

    def __init__(self, code_digit, min_length=1, max_length=6):
        self.code_digit = code_digit
        self.message = f"Code digit is not in ({min_length}, {max_length}) range"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.code_digit} -> {self.message}'
