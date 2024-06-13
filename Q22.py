def find_min_max(lst):
    return min(lst), max(lst)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
min_val, max_val = find_min_max(numbers)
print(f"The minimum value in the list is {min_val}.")
print(f"The maximum value in the list is {max_val}.")
