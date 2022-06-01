# Next.py- Exercise 3.4 by Amit Caspi 
import string

# Username contains illegal character exception
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username 

    def __str__(self):
        for i in range(len(self._username)):
            if (not(self._username[i].isalpha()) and (not(self._username[i].isdigit())) and (self._username[i] != "_")): 
                break
        return f'The username contains an illegal character "{self._username[i]}" at index {i}'

# Username's length is shorter then 3 exception
class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "The username is too short."

# Username's length is greater then 16 exception
class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "The username is too long."

# Password's length is shorter then 8 exception
class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password is too short."

# Password's length is greater then 40 exception
class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "The password is too long."

# Password missing required characters exception
class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return ("The password is missing a character ") 

# Password missing required character- Uppercase
class PasswordMissingUpper(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Uppercase)"

# Password missing required character- Lowercase
class PasswordMissingLower(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Lowercase)"

# Password missing required character- Digit (0-9)
class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Digit)"

# Password missing required character- Special (!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~)
class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Special)"

#--------------------------------------------------------------

def check_input(username, password):
    """
    The function prints "OK" if the username and password are correct and meet the relevant conditions.
    :param username: the username of the user
    :param password: the password of the user
    :type username: string 
    :type password: string
    :return: True / False, depending on- if the username and password are valid.
    :rtype: bool
    """
    result = string.punctuation
    try:
        # validate username
        for i in username:
            if i != "_" and not i.isdigit() and not i.isalpha():
                raise UsernameContainsIllegalCharacter(username) 
        if len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        # validate password
        elif (not(any(c.isupper() for c in password))): 
            raise PasswordMissingUpper(password) 
        elif (not(any(c.islower() for c in password))):
            raise PasswordMissingLower(password)
        elif (not((any(c.isdigit() for c in password)))):
            raise PasswordMissingDigit(password)
        elif (not(any(c in result for c in password))):
            raise PasswordMissingSpecial(password)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
    except Exception as e:
        print(e)
        return False
    else:
        print("OK")
        return True

def main():
    while True:
        user_name = input("Enter username: ")
        password = input("Enter password: ")
        if check_input(user_name, password): 
            break

if __name__ == '__main__':
    main()

