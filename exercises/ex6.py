# Tuples
# Implement a function that takes a tuple of strings as input and returns a new tuple 
# containing only the strings that start with an uppercase letter.

def filter_uppercase_strings(strings):
    # Your code here
    # Create an empty list
    new_list = []
    # Loop through strings input
    for str in strings:
        # If the first char for every string is uppercase
        if str[0].isupper():
            # Add that string to the empty list
            new_list.append(str)
    # Turn the list into a tuple and return that tuple
    return tuple(new_list)
    pass


# Test the function
strings = ("Apple", "banana", "Cat", "dog", "Elephant", "Frog")
print(filter_uppercase_strings(strings))  # Expected output: ("Apple", "Cat", "Elephant")





