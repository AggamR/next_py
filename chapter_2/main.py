from animals import *


def main():
    """
    Main function - the entry point of the program.
    """
    # initialising first animals
    brownie = Dog('Brownie', 10)
    zelda = Cat('Zelda', 3)
    stinky = Skunk('Stinky')
    keith = Unicorn('Keith', 7)
    lizzy = Dragon('Lizzy', 1450)

    # initialising 2nd gen animals
    doggo = Dog('Doggo', 80)
    kitty = Cat('Kitty', 80)
    stinky_jr = Skunk('Stinky Jr.', 80)
    clair = Unicorn('Clair', 80)
    mcfly = Dragon('McFly', 80)

    # not sure if I was supposed to initiate them in the list
    # or as seperate variables first...
    zoo_lst = [brownie, zelda, stinky, keith, lizzy,
               doggo, kitty, stinky_jr, clair, mcfly]

    for animal in zoo_lst:
        # print animal if animal is hungry
        if animal.is_hungry():
            print(f'{type(animal).__name__} {animal.get_name()}')
        # feed if hungry
        while animal.is_hungry():
            animal.feed()
        # talk and do the special method
        animal.talk()
        animal.special_method()


if __name__ == '__main__':
    main()
