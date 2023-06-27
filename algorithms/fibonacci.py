# Write a function that generates the Fibonacci sequence up to a given number n.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
# starting with 0 and 1.
#
# RETURNS an int

def generate_fib(n):
    # TODO: Generate the Fibonacci sequence up to n
    # sequence = [0,1]
    # # while n <= sequence[-1]:
    # for num in sequence:
    #     print(num)
    #     sum = num + num+1
    #     print (sum)
    # #         sequence.append(sum)
    # # return sequence


    # # Or:
    # Create a list
    sequence = []
    a = 0
    b = 1
    # Add to list, of fib sequence, until n or before n
    while a <= n:
        sequence.append(a)
        # a = b
        # b = a + b
        a, b = b, a+b
    # return list
    return sequence


# Test the function with the following code
n = int(input("Enter the number: "))
fib_sequence = generate_fib(n)
print("Fibonacci sequence up to", n, ":", fib_sequence)

