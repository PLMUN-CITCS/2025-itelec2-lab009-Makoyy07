user_input = input("Enter a number: ")
number = int(user_input)

try:
    user_input = input("Enter a number: ")
    number = int(user_input)  # Sinusubukang i-convert sa integer

    if number % 2 == 0:
        print("The number", number, "is Even.")
    else:
        print("The number", number, "is Odd.")

except ValueError:
    print("Invalid input. Please enter an integer.")  # Lalabas kung hindi valid ang input
