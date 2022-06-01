# Next.py- Exercise 2.5 by Amit Caspi 

class Animal:
    """
    A class that used to represent an animal
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger = 0):
        """
        This function is an Initialization method which is used to determine initial values
        for the characteristics of the animal.
        :param name: The name of animal.
        :type name: string
        :param hunger: The degree of hunger.
        :type hunger: int
        :return: None
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        This function returns the name of the animal.
        :return: The name of animal.
        :rtype: string
        """
        return self._name

    def is_hungry(self):
        """
        This function check and returns a Boolean value that describes whether the animal is hungry or not 
        (a hungry animal is an animal whose value of hunger is greater than zero).
        :return: True if the animal is hungery, false otherwise.
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self):
        """
        This function feed the animal and reduces the degree of hunger of the animal by one "point".
        :return: None.
        """
        self._hunger -= 1

    def talk(self, message):
        """
        This function gets a message and prints it.
        :param message: The message to print.
        :type message: string
        :return: None.
        """
        print(message)


class Dog(Animal):
    """
    A class that used to represent a dog
    """

    def __init__(self, name, hunger = 0):
        """
        This function initializes the dog.
        :param name: The name of the dog.
        :type name: string
        :param hunger: The degree of hunger.
        :type hunger: int
        :return: None
        """
        super().__init__(name, hunger)

    def talk(self):
        """
        This function call to function that prints the words that the dog knows how to say.
        :return: None.
        """
        super().talk('woof woof')

    def fetch_stick(self):
        """
        This function prints certain caption that spacial to the dog.
        :return: None.
        """
        print('There you go, sir!')


class Cat(Animal):
    """
    A class that used to represent a cat
    """

    def __init__(self, name, hunger = 0):
        """
        This function initializes the cat.
        :param name: The name of cat.
        :param hunger: The degree of hunger.
        :type hunger: int
        :return: None
        """
        super().__init__(name, hunger)

    def talk(self):
        """
        This function call to function that prints the words that the cat knows how to say.
        :return: None.
        """
        super().talk('meow')

    def chase_laser(self):
        """
        This function prints certain caption that spacial to the cat.
        :return: None.
        """
        print('Meeeeow')


class Skunk(Animal):
    """
    A class that used to represent a skunk
    """

    def __init__(self, name, hunger = 0, stink_count = 6):
        """
        This function initializes the skunk.
        :param name: The name of skunk.
        :param hunger: The degree of hunger.
        :type hunger: int
        :param stink_count: The count of stinking.
        :return: None
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        This function call to function that prints the words that the skunk knows how to say.
        :return: None.
        """
        super().talk('tsssss')

    def stink(self):
        """
        This function prints certain caption that spacial to the skunk.
        :return: None.
        """
        print('Dear lord!')


class Unicorn(Animal):
    """
    A class that used to represent a unicorn
    """

    def __init__(self, name, hunger = 0):
        """
        This function initializes the unicorn.
        :param name: The name of unicorn.
        :param hunger: The degree of hunger.
        :type hunger: int
        :return: None
        """
        super().__init__(name, hunger)

    def talk(self):
        """
        This function call to function that prints the words that the unicorn knows how to say.
        :return: None.
        """
        super().talk('Good day, darling')

    def sing(self):
        """
        This function prints certain caption that spacial to the unicorn.
        :return: None.
        """
        print('I’m not your toy...')


class Dragon(Animal):
    """
    A class that used to represent a dragon
    """

    def __init__(self, name, hunger = 0, color = "Green"):
        """
        This function initializes the dragon.
        :param name: The name of dragon.
        :param hunger: The degree of hunger.
        :type hunger: int
        :param color: the color of dragon.
        :return: None
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        """
        This function call to function that prints the words that the dragon knows how to say.
        :return: None.
        """
        super().talk('Raaaawr')

    def breath_fire(self):
        """
        This function prints certain caption that spacial to the dragon.
        :return: None.
        """
        print('$@#$#@$')


def main():
    dog_brownie = Dog("Brownie", 10)
    cat_zelda = Cat("Zelda", 3)
    skunk_stinky = Skunk("Stinky")
    unicorn_keith = Unicorn("Keith", 7)
    dragon_lizzy = Dragon("Lizzy", 1450)

    zoo_lst = [dog_brownie, cat_zelda, skunk_stinky, unicorn_keith, dragon_lizzy]

    dog_doggo = Dog('Doggo', 80)
    cat_kitty = Cat('Kitty', 80)
    skunk_stinky_jr = Skunk('Stinky Jr.', 80)
    unicorn_claire = Unicorn('Claire', 80)
    dragon_mcfly = Dragon('McFly', 80)

    zoo_lst += [dog_doggo, cat_kitty, skunk_stinky_jr, unicorn_claire, dragon_mcfly]

    print("\nThe type and name of the hungry animals\n(and all talks & special methods):\n")
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.__class__.__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print("\nThe name of the zoo is:", Animal.zoo_name)

if __name__ == '__main__':
    main()
