def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

number = int(input("Enter a number: "))
sum_digits = sum_of_digits(number)
print(f"The sum of the digits of {number} is {sum_digits}.")
