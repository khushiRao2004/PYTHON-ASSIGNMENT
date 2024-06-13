def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()
if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius)}")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"Temperature in Celsius: {fahrenheit_to_celsius(fahrenheit)}")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
