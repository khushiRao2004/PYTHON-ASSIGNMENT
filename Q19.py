import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

user_input = input("Enter a string: ")
no_punctuation_string = remove_punctuation(user_input)
print("String without punctuation:", no_punctuation_string)
