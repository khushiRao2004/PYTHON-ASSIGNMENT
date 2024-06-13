def count_occurrences(element, lst):
    return lst.count(element)

element = input("Enter the element to count: ")
lst = input("Enter a list of elements separated by spaces: ").split()
occurrences = count_occurrences(element, lst)
print(f"The element '{element}' occurs {occurrences} times in the list.")
