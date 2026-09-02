"""
Author: Ryon Connery
Date: September 2, 2026

Program: Mortgage Calculation Program

Purpose:
This program calculates yearly mortgage payments and produces a
year-by-year payment schedule using the sum-of-the-years'-digits
method to allocate total interest over the duration of the mortgage.

Program Flow:
1. Prompt for and validate the mortgage amount, mortgage duration,
   and annual interest rate.
2. Calculate total interest and the fixed yearly payment.
3. Calculate the sum of the years' digits.
4. Loop through each mortgage year.
5. Calculate yearly interest, principal paid, and ending balance.
6. Print the completed schedule and ending totals.

Variables:
mortgage_amount - Original mortgage principal.
years - Number of years in the mortgage term.
rate_percent - Interest rate entered by the user.
rate - Interest rate converted to decimal form.
total_interest - Total interest paid over the mortgage.
yearly_payment - Fixed payment made each year.
sum_of_years - Sum of the years' digits.
starting_balance - Mortgage balance at the start of a year.
remaining_years - Number of weighted years remaining.
year_interest - Interest allocated to the current year.
principal_paid - Portion of yearly payment applied to principal.
ending_balance - Mortgage balance after the yearly payment.
total_principal_paid - Accumulated principal paid.
"""

ZERO_TOLERANCE = 0.005


def enter_data():
    """Prompt for and validate mortgage amount, years, and interest rate."""
    while True:
        try:
            mortgage_amount = float(input("Enter the mortgage amount: $"))
            if mortgage_amount <= 0:
                print("Error: Mortgage amount must be greater than $0.00.")
            else:
                break
        except ValueError:
            print("Error: Enter a valid numeric mortgage amount.")

    while True:
        try:
            years = int(input("Enter the number of years: "))
            if years <= 0:
                print("Error: Number of years must be a positive whole number.")
            else:
                break
        except ValueError:
            print("Error: Enter a valid whole-number mortgage term.")

    while True:
        try:
            rate_percent = float(
                input("Enter the interest rate as a percentage: ")
            )
            if rate_percent < 0:
                print("Error: Interest rate cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Enter a valid numeric interest rate.")

    return mortgage_amount, years, rate_percent


def calculate_initial_values(mortgage_amount, years, rate_percent):
    """Calculate and return decimal rate, total interest, and yearly payment."""
    rate = rate_percent / 100

    total_interest = (
        mortgage_amount
        * rate
        * years
        / 2
    )

    yearly_payment = (
        mortgage_amount
        + total_interest
    ) / years

    return rate, total_interest, yearly_payment


def calculate_sum_of_years(years):
    """Calculate the sum of the years' digits using a for loop."""
    sum_of_years = 0

    for year in range(1, years + 1):
        sum_of_years += year

    return sum_of_years


def print_heading(yearly_payment, total_interest, sum_of_years):
    """Print introductory calculations and the schedule headings."""
    print()
    print(f"Yearly Payment: ${yearly_payment:.2f}")
    print(f"Total Interest: ${total_interest:.2f}")
    print(f"Sum of Years Digits: {sum_of_years}")
    print()

    print(
        f"{'Year':>4}"
        f"{'Starting Balance':>20}"
        f"{'Year Interest':>18}"
        f"{'Principal Paid':>18}"
        f"{'Ending Balance':>18}"
    )


def calculate_schedule(
    mortgage_amount,
    years,
    total_interest,
    yearly_payment,
    sum_of_years
):
    """Loop through the mortgage term, calculate each year, and print the schedule."""
    starting_balance = mortgage_amount
    total_principal_paid = 0.0

    for year in range(1, years + 1):
        remaining_years = years - year + 1

        year_interest = (
            total_interest
            * remaining_years
            / sum_of_years
        )

        principal_paid = yearly_payment - year_interest
        ending_balance = starting_balance - principal_paid

        # Normalize insignificant floating-point residue to a clean zero balance.
        if abs(ending_balance) < ZERO_TOLERANCE:
            ending_balance = 0.0

        total_principal_paid += principal_paid

        print(
            f"{year:>4}"
            f"{starting_balance:>20.2f}"
            f"{year_interest:>18.2f}"
            f"{principal_paid:>18.2f}"
            f"{ending_balance:>18.2f}"
        )

        starting_balance = ending_balance

    return starting_balance, total_principal_paid


def print_ending_information(
    ending_balance,
    total_interest,
    total_principal_paid
):
    """Print final mortgage totals."""
    print()
    print(f"Ending Balance: ${ending_balance:.2f}")
    print(f"Total Interest Paid: ${total_interest:.2f}")
    print(f"Total Principal Paid: ${total_principal_paid:.2f}")


def main():
    """Control the overall mortgage calculation program."""
    print("**** Mortgage Calculation Program by Ryon Connery *****")
    print()
    print(
        "This program calculates yearly mortgage payments "
        "and produces a payment schedule."
    )
    print()

    mortgage_amount, years, rate_percent = enter_data()

    rate, total_interest, yearly_payment = calculate_initial_values(
        mortgage_amount,
        years,
        rate_percent
    )

    sum_of_years = calculate_sum_of_years(years)

    print_heading(
        yearly_payment,
        total_interest,
        sum_of_years
    )

    ending_balance, total_principal_paid = calculate_schedule(
        mortgage_amount,
        years,
        total_interest,
        yearly_payment,
        sum_of_years
    )

    print_ending_information(
        ending_balance,
        total_interest,
        total_principal_paid
    )


main()
