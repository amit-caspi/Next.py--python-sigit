# Next.py- Exercise 5.4 by Amit Caspi 
# A program that generates valid ID numbers  

def check_id_valid(id_number):
    """
    The function receives an ID number and returns true if it is valid, otherwise returns false.
    :param id_number: new id number to check
    :type id_number: integer
    :return: True if the id number is a valid and False otherwise
    :rtype: bool
    """
    sum_of_id = sum([int(odd) for odd in str(id_number)[::2]])
    lst_of_even = [(2 * int(even)) for even in str(id_number)[1::2]] 
    for num in lst_of_even:
        if int(num) < 9:
            sum_of_id += num
        else:
            for digit in str(num):
                sum_of_id += int(digit)
    return sum_of_id % 10 == 0  # returns True if the sum is divided by 10

class IDIterator:
    """
    A class for creating iterators that create valid ID numbers
    """

    def __init__(self, id_number): 
        """
        This function initializes the ID.
        :param id_number: Id number to initialize the _id attribute
        :type: integer
        :return: None
        :rtype: None
        """
        self._id = id_number  

    def __iter__(self):
        """ 
        A method that returns the iterator instance (Iterator Protocol).
        :return: The object that triggered the method
        :rtype: IDIterator
        """
        return self

    def __next__(self):
        """ 
        A method that returns the next valid ID number (range between id_ and 999999999) and updates _id to it.
        :return: The next valid ID number 
        :rtype: integer
        :raise: StopIteration: If we passed 999999999 in search for the next valid id number.
        """
        for i in range(self._id + 1, 999999999 + 1): 
            if check_id_valid(i):
                self._id = i
                return self._id
        # A StopIteration exception is thrown at the end of the range (ID number 999999999)-
        raise StopIteration()

def id_generator(id_number):
    """
    The generator function receives an ID number and whenever it is asked to generate a value,
	it generates the next valid ID number in the range (up to 999999999).
    :param id_number: The id number (for generation)
    :type: integer
    :return: a generator that creates valid ID numbers
    :rtype: generator
    """
    for id in range(id_number + 1, 999999999 + 1): 
        if check_id_valid(id):
            yield id  

def main():
	# The main function
    user_id = input("Please enter an ID number (Consists of exactly 9 digits): ") 
    if not user_id.isnumeric():  # not numeric
        raise Exception("Wrong Input! An integer must be entered.")
    if len(user_id) != 9:  # not 9 digits of ID
        raise Exception("Wrong Input! ID Length Error- ID must have exactly 9 digits.")
    gen_or_iter = input("Generator or Iterator (gen/it)?: ")
    if gen_or_iter == "it":
        iterable_id = IDIterator(int(user_id)) # creating an iterator
    elif gen_or_iter == "gen":
        iterable_id = id_generator(int(user_id)) # creating a generator
    else:
        raise Exception("Wrong Input! not entered gen/it.")
    print("\n10 numbers of new IDs using", gen_or_iter, "are:\n")
    for i in range(10):  
        print(next(iterable_id))
 

if __name__ == '__main__':
    main()
