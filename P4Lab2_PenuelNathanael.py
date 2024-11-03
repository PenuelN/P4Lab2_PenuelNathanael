# P4Lab2_PenuelNathanael.py
def display_multiplication_table(num):
    # For loop to display the multiplication table from 1 to 12
    for i in range(1, 13):
        print(f"{num} * {i} = {num * i}")

while True:
    # Prompt for integer
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # Check if the number is negative
    if number < 0:
        print("This program does not handle negative numbers.")
    else:
        # Display the multiplication table if the number is 0 or higher
        display_multiplication_table(number)

    # Ask the user if they want to run the program again
    run_again = input("\nWould you like to run the program again? (yes/no): ").strip().lower()
    if run_again != "yes":
        print("Exiting program...")
        break
