def string_to_list(string):
    return list(string)

user_input = input("Enter a string: ")
char_list = string_to_list(user_input)
print("List of characters:", char_list)
