def check_id_valid(id_number):
    """
    Check if a given ID number is valid based on validation algorithm.

    Args:
        id_number (int): The ID to check.

    Returns:
        bool: Whether or no the id_number is valid
    """
    # one liner is split into a 2-liner, for PEP8
    # for each dig - (multiply by 2/1) - turn into string and sum THOSE digits
    # then, sum the entire thing
    # weirdest part  - [1, 2][i % 2]
    #       - if index even (%2=0) - 2, if odd (%2=1) - 1
    # (numbers to be mult by [1, 2] are reversed
    #       because index counts from 0 not 1)
    return sum([sum([int(ddig) for ddig in str(int(dig)*([1, 2][i % 2]))])
                for i, dig in enumerate(str(id_number))]) % 10 == 0


class IDIterator:
    """
    An iterator class that generates valid ID numbers.

    This class generates valid IDs numbers starting from an initial value
    until reaches the maximum (999999999).
    """
    def __init__(self, id):
        """
        Initialize the IDIterator with a starting ID number.

        Args:
            id (int): starting ID number.
        """
        self._id = id

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            IDIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Get the next valid ID number.

        Returns:
            int: next valid ID number.

        Raises:
            StopIteration: If ID reached max (max 9-digits num).
        """
        if self._id > 999999999:
            raise StopIteration

        self._id += 1

        # add untill good id
        while self._id < 999999999 and not check_id_valid(self._id):
            self._id += 1

        # didn't reach max
        if check_id_valid(self._id):
            return self._id

        # reached max
        raise StopIteration


def id_generator(id):
    """
    A generator function that yields valid IDs.

    Args:
        id (int): starting ID number.

    Yields:
        int: next valid ID number.

    Raises:
        StopIteration: If ID reached max (max 9-digits num).
    """
    while id < 999999999:
        while id < 999999999 and not check_id_valid(id):
            id += 1
        if id > 999999999:
            raise StopIteration
        yield id
        id += 1


def main():
    """
    Main function - program's entry point.
    Gets ID as an input, and generates the subsequent 10 valid IDs
    using either a generator, or an iterator object
    - depending on the user's choise
    """
    initid = int(input('Enter ID: '))
    whichtype = input('Generator or Iterator? (gen/it)? ')

    # generalised way of getting iterator/generator
    iditer = {
        'it': iter(IDIterator(initid)),
        'gen': id_generator(initid)
    }[whichtype]

    # print next 10
    for i in range(10):
        print(next(iditer))


if __name__ == '__main__':
    main()
