# Taking a number as input from the user
number = int(input("Enter a number: "))

# Calculating the factorial
factorial = 1
for i in range(1, number + 1):
    factorial *= i

# Printing the factorial
print(f"The factorial of {number} is {factorial}.")
