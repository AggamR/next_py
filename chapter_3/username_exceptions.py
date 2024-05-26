class UsernameContainsIllegalCharacter(Exception):
    """
    An exception to be raised when the username contains illegal characters.

    Attributes:
        illegal_char (str): The illegal character found in the username.
        index (int): The index position of
            the illegal character in the username.
    """

    def __init__(self, illegal_char, index):
        """
        Initialize the exception with the illegal character and its index.

        Args:
            illegal_char (str): The illegal character.
            index (int): The index position of the illegal character.
        """
        self.illegal_char = illegal_char
        self.index = index

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception.
        """
        return 'Username contains an illegal character ' \
            + f'"{self.illegal_char}" at index {self.index}'

    def get_arg(self):
        """
        Return the illegal character.

        Returns:
            str: The illegal character.
        """
        return self.illegal_char

    def print_arg(self):
        """
        Print the illegal character.
        """
        print(self.get_arg())


class UsernameTooShort(Exception):
    """
    An exception to be raised when the username is too short.

    Attributes:
        length (int): The length of the username.
    """

    def __init__(self, length):
        """
        Initialize the exception with the length of the username.

        Args:
            length (int): The length of the username.
        """
        self.length = length

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception.
        """
        return f'Username is too short. Length: {self.length}'

    def get_arg(self):
        """
        Return the length of the username.

        Returns:
            int: The length of the username.
        """
        return self.length

    def print_arg(self):
        """
        Print the length of the username.
        """
        print(self.get_arg())


class UsernameTooLong(Exception):
    """
    An exception to be raised when the username is too long.

    Attributes:
        length (int): The length of the username.
    """

    def __init__(self, length):
        """
        Initialize the exception with the length of the username.

        Args:
            length (int): The length of the username.
        """
        self.length = length

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception.
        """
        return f'Username is too long. Length: {self.length}'

    def get_arg(self):
        """
        Return the length of the username.

        Returns:
            int: The length of the username.
        """
        return self.length

    def print_arg(self):
        """
        Print the length of the username.
        """
        print(self.get_arg())
