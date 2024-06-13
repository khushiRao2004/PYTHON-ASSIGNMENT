def character_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

user_input = input("Enter a string: ")
frequency = character_frequency(user_input)
print("Character frequency:")
for char, freq in frequency.items():
    print(f"{char}: {freq}")
