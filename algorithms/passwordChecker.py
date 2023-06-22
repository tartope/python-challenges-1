import re

# Write a function that takes a password as input and checks its strength based on the following criteria:
#
# At least 8 characters long
# Contains both uppercase and lowercase letters
# Includes at least one digit
#
# The function should RETURN a boolean value indicating whether the password meets the criteria.

def check_password_strength(password):
    # TODO: Implement the password strength checking logic

    # With Regex:
    # password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    # match = password_regex.search(password)
    # # if match:
    # #     return True
    # # else:
    # #     return False

    # # Or:
    # return bool(match)

    # Without Regex:
    uppercase = False
    lowercase = False
    digit = False

    for ele in password:
        if len(password) >= 8:
            if ele.isalpha() and ele.isupper():
                uppercase = True
            elif ele.isalpha() and ele.islower():
                lowercase = True
            elif ele.isnumeric():
                digit = True
        else:
            return False
    if uppercase == True and lowercase == True and digit == True:
        return True
    else:
        return False
    pass

# Test the function
password = input("Enter a password: ")
is_strong = check_password_strength(password)
print("Is the password strong?", is_strong)
