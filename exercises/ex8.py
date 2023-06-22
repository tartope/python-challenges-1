# Dicts
# Implement a function that takes a dictionary of student names and their ages as input 
# and returns the name of the oldest student.

def find_oldest_student(students):
    # Your code here
    # Make age variable and set to 0
    age = 0
    # Make result variable and set to empty string
    name = ""
    # Loop through dict keys/values
    for k, v in students.items():
        # If value is greater than age
        if v > age:
            # Assign value to age
            age = v
            # Assign key to result
            name = k
    # Return reslut
    return name
    pass


# Test the function
students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22}
print(find_oldest_student(students))  # Expected output: "David"
