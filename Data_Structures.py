"""
Author: Ryon Connery
Date: September 3, 2026

Program: Data Structure Program

Purpose:
This program demonstrates the four Python data structures required for
Assessment 7: lists, tuples, sets, and dictionaries. A menu allows the
user to select a data-structure demonstration or exit the program.

Program Flow:
1. Display a menu with List, Tuple, Set, Dictionary, and Exit options.
2. For a list, display the original data, add an item, update an item,
   delete an item, and display the list after each operation.
3. For a tuple, display the hardcoded tuple data and demonstrate item
   retrieval.
4. For a set, display the original data, add an item, update an item,
   delete an item, and display the set after each operation.
5. For a dictionary, display at least five key-value fields.
6. Continue displaying the menu until the user selects Exit.
"""


def display_menu():
    """Display the five required menu choices."""
    print()
    print("Data Structure Program Menu")
    print("---------------------------")
    print("1. List Example")
    print("2. Tuple Example")
    print("3. Set Example")
    print("4. Dictionary Example")
    print("5. Exit")


def get_menu_choice():
    """Prompt for and validate a menu choice from 1 through 5."""
    while True:
        choice = input("Enter your choice (1-5): ").strip()

        if choice in {"1", "2", "3", "4", "5"}:
            return choice

        print("Error: Invalid menu selection. Enter a number from 1 through 5.")


def list_example():
    """Demonstrate list display, append, update, and delete operations."""
    fruits = ["Apple", "Banana", "Strawberry"]

    print()
    print("List Demonstration")
    print("------------------")
    print(f"Original list: {fruits}")

    new_fruit = input("Enter a new fruit to append: ").strip()

    if new_fruit:
        fruits.append(new_fruit)
        print(f"List after append: {fruits}")
    else:
        print("Error: A blank value cannot be added.")
        print(f"List remains: {fruits}")

    while True:
        item_to_update = input("Enter the fruit to update: ").strip()

        if item_to_update in fruits:
            replacement = input(
                f"Enter the replacement for {item_to_update}: "
            ).strip()

            if replacement:
                index = fruits.index(item_to_update)
                fruits[index] = replacement
                print(f"List after update: {fruits}")
                break

            print("Error: A blank replacement cannot be used.")
        else:
            print("Error: That fruit is not in the list.")

    while True:
        item_to_delete = input("Enter the fruit to delete: ").strip()

        if item_to_delete in fruits:
            fruits.remove(item_to_delete)
            print(f"List after delete: {fruits}")
            break

        print("Error: That fruit is not in the list.")


def tuple_example():
    """Demonstrate tuple storage, printing, and item retrieval."""
    cities = ("Charlotte", "New York", "Chicago", "Seattle", "Denver")

    print()
    print("Tuple Demonstration")
    print("-------------------")
    print(f"Tuple contents: {cities}")
    print(f"First city: {cities[0]}")
    print(f"Third city: {cities[2]}")
    print(f"Last city: {cities[-1]}")


def set_example():
    """Demonstrate set display, add, update, and delete operations."""
    states = {"North Carolina", "Virginia", "Georgia", "Florida"}

    print()
    print("Set Demonstration")
    print("-----------------")
    print(f"Original set: {sorted(states)}")

    while True:
        new_state = input("Enter a new state to add: ").strip()

        if not new_state:
            print("Error: A blank value cannot be added.")
        elif new_state in states:
            print("Error: That state is already in the set.")
        else:
            states.add(new_state)
            print(f"Set after add: {sorted(states)}")
            break

    while True:
        state_to_update = input("Enter the state to update: ").strip()

        if state_to_update not in states:
            print("Error: That state is not in the set.")
            continue

        replacement = input(
            f"Enter the replacement for {state_to_update}: "
        ).strip()

        if not replacement:
            print("Error: A blank replacement cannot be used.")
        elif replacement in states:
            print("Error: The replacement already exists in the set.")
        else:
            states.remove(state_to_update)
            states.add(replacement)
            print(f"Set after update: {sorted(states)}")
            break

    while True:
        state_to_delete = input("Enter the state to delete: ").strip()

        if state_to_delete in states:
            states.remove(state_to_delete)
            print(f"Set after delete: {sorted(states)}")
            break

        print("Error: That state is not in the set.")


def dictionary_example():
    """Demonstrate dictionary storage and key-value retrieval."""
    city = {
        "City": "Berlin",
        "Country": "Germany",
        "Population": 3_755_251,
        "Language": "German",
        "Currency": "Euro",
        "Continent": "Europe"
    }

    print()
    print("Dictionary Demonstration")
    print("------------------------")
    print("Dictionary fields and values:")

    for key, value in city.items():
        print(f"{key}: {value}")


def main():
    """Control the overall execution of the data-structure program."""
    print("**** Data Structure Program by Ryon Connery *****")
    print()
    print(
        "This program demonstrates Python lists, tuples, sets, "
        "and dictionaries."
    )
    print(
        "Select a menu option to view and work with the corresponding "
        "data structure."
    )

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            list_example()

        elif choice == "2":
            tuple_example()

        elif choice == "3":
            set_example()

        elif choice == "4":
            dictionary_example()

        elif choice == "5":
            print()
            print("Program ended. Have a good day.")
            break


main()
