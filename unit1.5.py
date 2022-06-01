# Next.py- Exercise 1.5 by Amit Caspi 

def longest_name(file):
    """
    The function prints the longest name in a file.
    :param file: A file that contains a list of names, one name per line.
    :type file: str- txt file
    :return: None
    """
    with open(file, 'r') as f:
        print("Longest name: ", max(f.read().split('\n'), key=len))


def sum_all_lens(file):
    """
    The function prints the sum of the lengths of the names in the file.
    :param file: A file that contains a list of names, one name per line.
    :type file: str- txt file
    :return: None
    """
    with open(file, 'r') as f:
	    print("Sum of all names lengths: ", sum(map(lambda name: len(name), f.read().split('\n'))))


def shortest_names(file):
    """
    The function prints the shortest names in the file, each name in a separate line.
    :param file: A file that contains a list of names, one name per line.
    :type file: str- txt file
    :return: None
    """
    with open(file, 'r') as f:
        print("Shortest names:\n", '\n '.join(name for name in f.read().split('\n') if len(name) == len(min(open(file, 'r').read().split('\n'), key=len))))


def lens_of_words(file):
    """
    The function prints the longest name in a file.
    :param file: A file that contains a list of names, one name per line.
    :type file: str- txt file
    :return: None
    """
    with open(file, 'r') as f:
        with open("name_length.txt", 'w+') as lens_words_file:
            lens_words_file.write('\n '.join(map(str, [len(name) for name in f.read().split('\n')])))
            #lens_words_file.write('\n '.join([str(len(x)-1) for x in f]))


def name_in_specific_len(file):
    """
    The function receives from the user a number that represents the length of a name, 
    and prints all the names in the file that are that length.
    :param file: A file that contains a list of names, one name per line.
    :type file: str- txt file
    :return: None
    """
    word_length = int(input("Enter a number that represents the length of a name: "))
    with open(file, 'r') as f:
        print("The names in the file which have this length:\n", '\n '.join(name for name in f.read().split('\n') if len(name) == word_length))


longest_name("names.txt")
sum_all_lens("names.txt")
shortest_names("names.txt")
lens_of_words("names.txt")
with open("name_length.txt", 'r') as lens_words_file:
    print("Length of each name in the file:\n", lens_words_file.read())
name_in_specific_len("names.txt")