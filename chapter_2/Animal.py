class Animal:
    """
    A class representing an animal in a zoo.

    Attributes:
        zoo_name (str): The name of the zoo where the animal is located.
    """

    zoo_name = 'Hayaton'

    def __init__(self, name, hunger=0):
        """
        Initialize an Animal object.

        Args:
            name (str): The animal's name.
            hunger (int, optional): The initial hunge
                level of the animal. 0 by default.
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Get the animal's name.

        Returns:
            str: The animal's name.
        """
        return self._name

    def is_hungry(self):
        """
        Check if the animal is hungry.

        Returns:
            bool: Whether or not the animal is hungry.
        """
        return self._hunger > 0

    def feed(self):
        """
        Feed the animal, (reduce its hunger level by 1).
        """
        self._hunger -= 1

    def talk(self):
        """
        Make the animal talk.

        This is a placeholder method that does nothing.
        It's overridden in subclasses to implement specific behavior.
        """
        pass

    def special_method(self):
        """
        A special method - different for each animal.

        This is a placeholder method that does nothing.
        It's overridden in subclasses to implement specific behavior.
        """
        pass
