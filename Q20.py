def sum_of_list(numbers):
    return sum(numbers)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
total = sum_of_list(numbers)
print("The sum of the numbers is:", total)
