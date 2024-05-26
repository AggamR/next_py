def gen_secs():
    """
    Generator that yields seconds (0 to 59).

    Yields:
        int: The next second in the range.
    """
    second = 0
    while second < 60:
        yield second
        second += 1


def gen_minutes():
    """
    Generator that yields minutes (0 to 59).

    Yields:
        int: The next minute in the range.
    """
    minute = 0
    while minute < 60:
        yield minute
        minute += 1


def gen_hours():
    """
    Generator that yields hours (1 to 23).

    Yields:
        int: The next hour in the range.
    """
    hour = 0
    while hour < 24:
        yield hour
        hour += 1


def gen_time():
    """
    Generator that yields all possible time strings in HH:MM:SS format.

    Yields:
        str: The next time string.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield '%02d:%02d:%02d' % (hour, minute, second)


# since example showed =2019 I assumed it shouoldn't be automatic
# if it should've been it would be start=date.today().year
# [you'd need "from datetime import date" though]
def gen_years(start=2024):
    """
    Generator that yields years, starting from a given start year.

    Args:
        start (int): The starting year (defaults to 2024).

    Yields:
        int: The next year, starting from the given start year
            (2024 if none supplied).
    """
    while True:
        yield start
        start += 1


def gen_months():
    """
    Generator that yields months (1 to 12).

    Yields:
        int: The next month in the range.
    """
    month = 1
    while month <= 12:
        yield month
        month += 1


def gen_days(month, leap_year=True):
    """
    Generator that yields days for a given month
    (accounts for leap years and days in each month).

    Args:
        month (int): The month for which to generate days (1-12).
        leap_year (bool): whether on not it's a leap year (True by default).

    Yields:
        int: The next day in the month.
    """
    # default = 31
    days = 31

    # check if month has 30 days (one of these options)
    if month in [11, 9, 6, 4]:
        days = 30
    # check if month is Feb
    elif month == 2:
        days = 29 if leap_year else 28

    # actual generator
    day = 1
    while day <= days:
        yield day
        day += 1


# while exaple didn't show a year argument
# I thought it would make sense since the gen_years
# function can get a start argument
def gen_date(start_year=2024):
    """
    Generator that yields all possible date strings
    in DD/MM/YYYY HH:MM:SS format, starting from a given start year.

    Args:
        start_year (int): The starting year (2024 by default).

    Yields:
        str: The next date string.
    """
    for year in gen_years(start_year):
        for month in gen_months():
            # {year % 4 == 0} determines if it's a leap year
            for day in gen_days(month, year % 4 == 0):
                for time in gen_time():
                    yield '%02d/%02d/%d %s' % (day, month, year, time)


def main():
    """
    Main function - entry point of the program.
    generates dates and prints every milionth date.
    """
    dategen = gen_date()
    count = 0
    while True:
        result = next(dategen)
        # tries using modulo operator but always came weird
        if count == 1000000:
            print(result)
            count = 0
        count += 1


if __name__ == '__main__':
    main()
