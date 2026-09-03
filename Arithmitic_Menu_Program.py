"""
Author: Ryon Connery
Date: September 3, 2026

Program: Imperative Arithmetic Menu Program

Purpose:
This program demonstrates the imperative programming paradigm in Python.
It repeatedly displays a menu that allows the user to select addition,
subtraction, multiplication, division, or remainder. The program obtains
two numeric values, calls the appropriate arithmetic function, displays
the result, and continues until the user chooses to exit.

Program Flow:
1. Display the arithmetic-operation menu.
2. Validate the user's menu selection.
3. Prompt for and validate two numeric values.
4. Call the function associated with the selected operation.
5. Check the second number before division or remainder.
6. Display the result or an appropriate error message.
7. Ask whether the user wishes to exit.
8. Repeat until the user chooses to end the program.
"""


def add(x, y):
    """Return the sum of two numbers."""
    return x + y


def subtract(x, y):
    """Return the difference between two numbers."""
    return x - y


def multiply(x, y):
    """Return the product of two numbers."""
    return x * y


def divide(x, y):
    """
    Return the quotient of two numbers.

    The second number is the denominator and must not be zero.
    """
    if y == 0:
        return None

    return x / y


def remainder(x, y):
    """
    Return the remainder after dividing the first number by the second.

    The second number is the denominator and must not be zero.
    """
    if y == 0:
        return None

    return x % y


def get_number(prompt):
    """Prompt until the user enters a valid numeric value."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Enter a valid numeric value.")


def get_menu_choice():
    """Display the menu and return a validated selection from 1 through 5."""
    while True:
        print()
        print("Arithmetic Operations Menu")
        print("--------------------------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")

        choice = input("Enter your choice (1-5): ").strip()

        if choice in {"1", "2", "3", "4", "5"}:
            return choice

        print("Error: Invalid menu selection. Enter a number from 1 through 5.")


def format_result(value):
    """
    Format numeric results for clear user-facing output.

    Whole-number results are displayed without an unnecessary decimal,
    while fractional results retain significant decimal digits.
    """
    if value.is_integer():
        return str(int(value))

    return f"{value:.10g}"


def perform_operation(choice, x, y):
    """Perform the selected arithmetic operation and display its result."""

    if choice == "1":
        result = add(x, y)
        print(f"Result: {format_result(result)}")

    elif choice == "2":
        result = subtract(x, y)
        print(f"Result: {format_result(result)}")

    elif choice == "3":
        result = multiply(x, y)
        print(f"Result: {format_result(result)}")

    elif choice == "4":
        result = divide(x, y)

        if result is None:
            print("Error: Division by zero is undefined.")
        else:
            print(f"Result: {format_result(result)}")

    elif choice == "5":
        result = remainder(x, y)

        if result is None:
            print("Error: Remainder division by zero is undefined.")
        else:
            print(f"Result: {format_result(result)}")


def ask_to_exit():
    """Ask whether the user wants to exit and return True for yes."""
    while True:
        response = input("Do you wish to exit? (yes/no): ").strip().lower()

        if response in {"yes", "y"}:
            return True

        if response in {"no", "n"}:
            return False

        print("Error: Enter yes or no.")


def main():
    """Control the overall execution of the imperative program."""

    print("**** Imperative Arithmetic Program by Ryon Connery *****")
    print()
    print(
        "This program performs addition, subtraction, multiplication, "
        "division, and remainder operations."
    )

    exit_program = False

    while not exit_program:
        choice = get_menu_choice()

        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        perform_operation(
            choice,
            first_number,
            second_number
        )

        print()
        exit_program = ask_to_exit()

    print()
    print("Program ended. Have a good day.")


main()
