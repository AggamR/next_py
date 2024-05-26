import string
from username_exceptions import *
from password_exceptions import *
from password_char_exceptions import *


def check_input(username, password):
    """
    Checks credentials validity.
    If credentials are valid - will print 'OK'.
    if credentials are invalid - will throw the appropriate Exception.
    """
    # check for illegal chars in username
    for i in range(len(username)):
        if username[i] not in string.ascii_letters + string.digits + '_':
            raise UsernameContainsIllegalCharacter(username[i], i)
    # check username length
    if len(username) < 3:
        raise UsernameTooShort(len(username))
    if len(username) > 16:
        raise UsernameTooLong(len(username))
    # check for missing chars in password
    if not any([char in string.ascii_uppercase for char in password]):
        raise PasswordMissingUppercase
    if not any([char in string.ascii_lowercase for char in password]):
        raise PasswordMissingLowercase
    if not any([char.isdigit() for char in password]):
        raise PasswordMissingDigit
    if not any([char in string.punctuation for char in password]):
        raise PasswordMissingSpecial
    # check pass length
    if len(password) < 8:
        raise PasswordTooShort(len(password))
    if len(password) > 40:
        raise PasswordTooLong(len(password))

    # no exceptions, print OK
    print('OK')


def test():
    """
    A function used to test all the options.
    """
    for option in [
        ('1', '2'),
        ('0123456789ABCDEFG', '2'),
        ('A_a1.', '12345678'),
        ('A_1', '2'),
        ('A_1', 'ThisIsAQuiteLongPasswordAndHonestlyUnnecessary'),
        ('A_1', 'abcdefghijklmnop'),
        ('A_1', 'ABCDEFGHIJLKMNOP'),
        ('A_1', 'ABCDEFGhijklmnop'),
        ('A_1', '4BCD3F6h1jk1mn0p'),
        ('A_1', '4BCD3F6.1jk1mn0p'),
    ]:
        try:
            check_input(*option)
        except Exception as e:
            print(e)


def main():
    """
    The program's entry point.
    a user is to enter username and password until they are valid.
    """
    while True:
        username = input('Enter username: ')
        password = input('Enter password: ')

        try:
            check_input(username, password)
        except Exception as e:
            # print error string so that the user knows what's wrong
            print(e)
        else:
            break

        # if got here, it didn't break
        print('Try again:')


if __name__ == '__main__':
    main()
