# Exercise 3: Loops
# TODO: Write code that prints all between 1 and n using a while loop
# TODO: Write code that prints all the even numbers between 1 and n using a for loop

def main(n):
    print("All numbers from 1 to n:")
    # use a while loop
    i = 1
    while i <= n:
        print(i)
        i += 1

    print("Even numbers between 1 and n:")
    # even numbers from 1-20 (for loop)
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)



main(12)