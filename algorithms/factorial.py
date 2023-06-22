# Write a function to calculate the factorial of a given number (n).
# hint: try recursion

def factorial(n):
   result = 1
   for num in range(2, n+1):
      result *= num
   return result

   pass



# Test case
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")

# Recursion practice:
# def log(num):
#    if num > 5:
#       return
#    print(num)
#    log(num+1)

# print(log(1))