from password_exceptions import PasswordMissingCharacter


class PasswordMissingUppercase(PasswordMissingCharacter):
    """
    An exception to be raised when the password
    is missing an uppercase character.
    """

    def __init__(self):
        """
        Initialize the exception for missing uppercase character.
        """
        super().__init__('Uppercase')

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception with specific details
                about the missing uppercase character.
        """
        return f'{super().__str__()} (Uppercase)'


class PasswordMissingLowercase(PasswordMissingCharacter):
    """
    An exception to be raised when the password
    is missing a lowercase character.
    """

    def __init__(self):
        """
        Initialize the exception for missing lowercase character.
        """
        super().__init__('Lowercase')

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception with specific details
                about the missing lowercase character.
        """
        return f'{super().__str__()} (Lowercase)'


class PasswordMissingDigit(PasswordMissingCharacter):
    """
    An exception to be raised when the password is missing a digit character.
    """

    def __init__(self):
        """
        Initialize the exception for missing digit character.
        """
        super().__init__('Digit')

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception with specific details
                about the missing digit character.
        """
        return f'{super().__str__()} (Digit)'


class PasswordMissingSpecial(PasswordMissingCharacter):
    """
    An exception to be raised when the password is missing a special character.
    """

    def __init__(self):
        """
        Initialize the exception for missing special character.
        """
        super().__init__('Special')

    def __str__(self):
        """
        Return the exceptions' string description.

        Returns:
            str: A description of the exception with specific details
                about the missing special character.
        """
        return f'{super().__str__()} (Special)'
