from Animal import Animal


class Dog(Animal):
    """
    A class representing a dog, which is a subclass of Animal.
    """

    def talk(self):
        """
        Make the dog bark (prints 'woof woof').
        """
        print('woof woof')

    def fetch_stick(self):
        """
        Make the dog fetch a stick (prints 'There you go, sir!').
        """
        print('There you go, sir!')

    def special_method(self):
        """
        A special method for the dog
        basically a wrapper for the fetch_stick method.
        """
        self.fetch_stick()


class Cat(Animal):
    """
    A class representing a cat, which is a subclass of Animal.
    """

    def talk(self):
        """
        Make the cat meow (prints 'meow').
        """
        print('meow')

    def chase_laser(self):
        """
        Make the cat chase a laser pointer (prints 'Meeeeow').
        """
        print('Meeeeow')

    def special_method(self):
        """
        A special method for the cat.
        basically a wrapper for the chase_laser method.
        """
        self.chase_laser()


class Skunk(Animal):
    """
    A class representing a skunk, which is a subclass of Animal.
    """

    def __init__(self, name, hunger=0, stink_count=6):
        """
        Initialize a Skunk object.

        Args:
            name (str): The name of the skunk.
            hunger (int, optional): The initial hunger level of the skunk.
                Defaults to 0.
            stink_count (int, optional): The number of
                stink the skunk has. Defaults to 6.
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        Make the skunk hiss (prints 'tsssss').
        """
        print('tsssss')

    def stink(self):
        """
        Make the skunk stink (prints 'Dear lord!').
        """
        print('Dear lord!')
        """
        # it wasn't clear whether or nor the function
        # can only run "stink_count" times
        # if so it would look like:
        if self.stink_count > 0:
            print('Dear lord!')
            self.stink_count -= 1
        """

    def special_method(self):
        """
        A special method for the skunk.
        basically a wrapper for the stink method.
        """
        self.stink()


class Unicorn(Animal):
    """
    A class representing a unicorn, which is a subclass of Animal.
    """

    def talk(self):
        """
        Make the unicorn talk (prints 'Good day, darling').
        """
        print('Good day, darling')

    def sing(self):
        """
        Make the unicorn sing (prints 'I'm not your toy...').
        """
        print('I\'m not your toy...')

    def special_method(self):
        """
        A special method for the unicorn.
        basically a wrapper for the sing method.
        """
        self.sing()


class Dragon(Animal):
    """
    A class representing a dragon, which is a subclass of Animal.
    """

    def __init__(self, name, hunger=0, color='Green'):
        """
        Initialize a Dragon object.

        Args:
            name (str): The name of the dragon.
            hunger (int, optional): The initial hunger level of the dragon.
                Defaults to 0.
            color (str, optional): The color of the dragon.
                Defaults to 'Green'.
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        Make the dragon roar (prints 'Raaaawr').
        """
        print('Raaaawr')

    def breath_fire(self):
        """
        Make the dragon breathe fire (prints '$@#$#@$').
        """
        print('$@#$#@$')

    def special_method(self):
        """
        A special method for the dragon.
        basically a wrapper for the breath_fire method.
        """
        self.breath_fire()
