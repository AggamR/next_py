class PasswordMissingCharacter(Exception):
    """
    Base class for exceptions raised when the password
    is missing a specific type of character.

    Attributes:
        missing_char_type (str): The type of missing character.
    """

    def __init__(self, missing_char_type):
        """
        Initialize the exception with the type of missing character.

        Args:
            missing_char_type (str): The type of missing character.
        """
        self.missing_char_type = missing_char_type

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception.
        """
        return 'Password is missing required character type: ' \
            + self.missing_char_type

    def get_arg(self):
        """
        Return the type of missing character.

        Returns:
            str: The type of missing character.
        """
        return self.missing_char_type

    def print_arg(self):
        """
        Print the type of missing character.
        """
        print(self.get_arg())


class PasswordTooShort(Exception):
    """
    An exception to be raised when the password is too short.

    Attributes:
        length (int): The length of the password.
    """

    def __init__(self, length):
        """
        Initialize the exception with the length of the password.

        Args:
            length (int): The length of the password.
        """
        self.length = length

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception.
        """
        return f'Password is too short. Length: {self.length}'

    def get_arg(self):
        """
        Return the length of the password.

        Returns:
            int: The length of the password.
        """
        return self.length

    def print_arg(self):
        """
        Print the length of the password.
        """
        print(self.get_arg())


class PasswordTooLong(Exception):
    """
    An exception to be raised when the password is too long.

    Attributes:
        length (int): The length of the password.
    """

    def __init__(self, length):
        """
        Initialize the exception with the length of the password.

        Args:
            length (int): The length of the password.
        """
        self.length = length

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception.
        """
        return f'Password is too long. Length: {self.length}'

    def get_arg(self):
        """
        Return the length of the password.

        Returns:
            int: The length of the password.
        """
        return self.length

    def print_arg(self):
        """
        Print the length of the password.
        """
        print(self.get_arg())
