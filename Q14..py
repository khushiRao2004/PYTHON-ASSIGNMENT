def read_lines():
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

print("Enter multiple lines of text (press Enter on an empty line to finish):")
user_lines = read_lines()
print("You entered:")
for line in user_lines:
    print(line)
