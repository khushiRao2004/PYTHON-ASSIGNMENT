# Taking a string input from the user
user_input = input("Enter a string: ")

# Writing the input to a text file
with open("output.txt", "w") as file:
    file.write(user_input)

print("The string has been written to output.txt")
