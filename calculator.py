# A simple command line calculator thatperforms addition and multiplication
def get_numbers():
    numbers = []
    print("Enter numbers one by one. Type 'done' when finished:")

    while True:
        user_input = input("Enter a number ").strip()
        if user_input.lower() == "done":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number")

    return numbers

def add_numbers(numbers):
    # Add all numbers in the list
    return sum(numbers)


def main():
    """
    Main function to run the calculator
    """
    print("=" * 50)
    print("Welcome to collaborative calculator")
    print("=" * 50)

    numbers = get_numbers()

    if len(numbers) == 0:
        print("No numbers enetered. Exiting!")
        return

    print(f"\nYou entered: {numbers}")
    print("\nWhat Operation would you like to perform?\n")
    print("1 - Add")
    print("2 - Multiply")

    choice = input("Enter your choice 1 or 2: ").strip()

    if choice == "1":
        result = add_numbers(numbers)
        print(f"\n result: {'+'.join(map(str,numbers))} = {result}")
    elif choice == "2":
        print("Multiplication feature by Gift coming soon")

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
