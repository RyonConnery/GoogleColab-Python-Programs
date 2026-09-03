"""
Author: Ryon Connery
Date: September 3, 2026

Program: Recursive Program

Purpose:
This program demonstrates recursion in Python using two examples:
factorial calculation and the Tower of Hanoi. The program displays a
three-option menu that allows the user to run either recursive example
or exit the program.

Program Flow:
1. Display introductory information.
2. Display a menu with Factorial, Tower of Hanoi, and Exit options.
3. For Factorial, prompt for a nonnegative integer and recursively
   calculate the factorial while displaying each recursive step.
4. For Tower of Hanoi, prompt for the number of rods, number of disks,
   start pole, end pole, and middle pole.
5. Recursively display each disk movement from the start pole to the
   end pole using the middle pole.
6. Return to the menu until the user selects Exit.
"""


def get_integer(prompt):
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Enter a valid whole number.")


def recur_factorial(number):
    """Recursively calculate factorial while displaying each recursive step."""
    print(f"Factorial step: {number}")

    if number <= 1:
        return 1

    return number * recur_factorial(number - 1)


def work_factorial():
    """Prompt for a number, validate it, and display its recursive factorial."""
    print()
    print("Factorial Demonstration")
    print("-----------------------")

    while True:
        number = get_integer("Enter a number to find the factorial: ")

        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            break

    result = recur_factorial(number)

    print()
    print(f"The factorial of {number} is {result}.")


def hanoi(number_of_disks, start_pole, end_pole, middle_pole):
    """Recursively move disks from the start pole to the end pole."""
    if number_of_disks == 1:
        print(
            f"Move disk 1 from pole {start_pole} "
            f"to pole {end_pole}."
        )
        return

    hanoi(
        number_of_disks - 1,
        start_pole,
        middle_pole,
        end_pole
    )

    print(
        f"Move disk {number_of_disks} from pole {start_pole} "
        f"to pole {end_pole}."
    )

    hanoi(
        number_of_disks - 1,
        middle_pole,
        end_pole,
        start_pole
    )


def get_tower_inputs():
    """Prompt for and validate the Tower of Hanoi configuration."""
    while True:
        number_of_rods = get_integer("Enter the number of rods: ")

        if number_of_rods < 3:
            print("Error: Tower of Hanoi requires at least 3 rods.")
        else:
            break

    while True:
        number_of_disks = get_integer("Enter the number of disks: ")

        if number_of_disks <= 0:
            print("Error: The number of disks must be greater than zero.")
        else:
            break

    while True:
        start_pole = get_integer("Enter the start pole: ")
        end_pole = get_integer("Enter the end pole: ")
        middle_pole = get_integer("Enter the middle pole: ")

        valid_range = (
            1 <= start_pole <= number_of_rods
            and 1 <= end_pole <= number_of_rods
            and 1 <= middle_pole <= number_of_rods
        )

        distinct_poles = len(
            {start_pole, end_pole, middle_pole}
        ) == 3

        if not valid_range:
            print(
                f"Error: Pole numbers must be between 1 "
                f"and {number_of_rods}."
            )
        elif not distinct_poles:
            print(
                "Error: The start, end, and middle poles "
                "must be different."
            )
        else:
            return (
                number_of_rods,
                number_of_disks,
                start_pole,
                end_pole,
                middle_pole
            )


def work_hanoi():
    """Collect Tower of Hanoi data and execute the recursive solution."""
    print()
    print("Tower of Hanoi Demonstration")
    print("----------------------------")

    (
        number_of_rods,
        number_of_disks,
        start_pole,
        end_pole,
        middle_pole
    ) = get_tower_inputs()

    print()
    print(f"Number of rods: {number_of_rods}")
    print(f"Number of disks: {number_of_disks}")
    print(
        f"Moving all disks from pole {start_pole} "
        f"to pole {end_pole} using pole {middle_pole}."
    )
    print()

    hanoi(
        number_of_disks,
        start_pole,
        end_pole,
        middle_pole
    )

    print()
    print(
        f"Tower of Hanoi complete. All {number_of_disks} disks "
        f"have been moved to pole {end_pole}."
    )


def display_menu():
    """Display the three required menu options."""
    print()
    print("Recursive Program Menu")
    print("----------------------")
    print("1. Factorial")
    print("2. Tower of Hanoi")
    print("3. Exit")


def main():
    """Control the overall execution of the recursive program."""
    print("**** Recursive Program by Ryon Connery *****")
    print()
    print(
        "This program demonstrates recursion using factorial "
        "and the Tower of Hanoi."
    )
    print(
        "Each example calls a function recursively until "
        "its stopping condition is reached."
    )

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            work_factorial()

        elif choice == "2":
            work_hanoi()

        elif choice == "3":
            print()
            print("Program ended. Have a good day.")
            break

        else:
            print("Error: Invalid menu selection. Enter 1, 2, or 3.")


main()
