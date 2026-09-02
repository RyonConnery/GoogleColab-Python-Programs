"""
Author: Ryon Connery
Date: September 1, 2026

Program: Functional Purchase Calculation Program

Purpose:
This program calculates the gross purchase amount, discount, tax,
shipping cost, and final amount paid. The program demonstrates the
use of user-defined Python functions by dividing the calculation
process into smaller, specialized tasks.

Variables:
unit_price - Price of one item entered by the user.
quantity - Number of items purchased.
gross_sale - Unit price multiplied by quantity.
discount_rate - Discount percentage selected by the program.
discount_amount - Dollar amount of the applicable discount.
total_after_discount - Gross sale minus the discount.
tax_amount - Six percent tax on the amount after discount.
shipping_cost - Two percent shipping cost.
total_amount_paid - Final amount after discount, tax, and shipping.
"""

LOW_DISCOUNT_RATE = 0.03
HIGH_DISCOUNT_RATE = 0.05
TAX_RATE = 0.06
SHIPPING_RATE = 0.02


def enter_data():
    """Prompt the user for the unit price and quantity purchased."""
    unit_price = float(input("Enter the price per item: $"))
    quantity = int(input("Enter the quantity purchased: "))
    return unit_price, quantity


def calc_gross_sale(unit_price, quantity):
    """Calculate and return the original purchase amount."""
    gross_sale = unit_price * quantity
    return gross_sale


def calc_discount(gross_sale):
    """Calculate and return the applicable discount amount and rate."""
    if gross_sale >= 100:
        discount_rate = HIGH_DISCOUNT_RATE
    else:
        discount_rate = LOW_DISCOUNT_RATE

    discount_amount = gross_sale * discount_rate

    return discount_amount, discount_rate


def calc_tax(total_after_discount):
    """Calculate and return the tax amount."""
    tax_amount = total_after_discount * TAX_RATE
    return tax_amount


def calc_shipping_cost(total_after_discount):
    """Calculate and return the shipping cost."""
    shipping_cost = total_after_discount * SHIPPING_RATE
    return shipping_cost


def calc_total_cost(
    gross_sale,
    discount_amount,
    tax_amount,
    shipping_cost
):
    """Calculate and return the discounted total and final amount paid."""
    total_after_discount = gross_sale - discount_amount

    total_amount_paid = (
        total_after_discount
        + tax_amount
        + shipping_cost
    )

    return total_after_discount, total_amount_paid


def print_results(
    gross_sale,
    discount_rate,
    discount_amount,
    total_after_discount,
    tax_amount,
    shipping_cost,
    total_amount_paid
):
    """Display all calculated purchase information."""
    print()
    print("Purchase Summary")
    print("----------------------------")
    print("Original Price: $", gross_sale)
    print("Discount Rate:", discount_rate * 100, "%")
    print("Discount Amount: $", discount_amount)
    print("Total After Discount: $", total_after_discount)
    print("Tax Amount: $", tax_amount)
    print("Shipping Cost: $", shipping_cost)
    print("Total Amount Paid: $", total_amount_paid)
    print()
    print("Thank you for using the program, Ryon Connery.")


def main():
    """Control the overall flow of the program."""
    print("Functional Purchase Calculation Program")
    print("This program calculates discounts, tax, shipping,")
    print("and the final purchase amount using Python functions.")
    print("Programmed by Ryon Connery")
    print()

    unit_price, quantity = enter_data()

    gross_sale = calc_gross_sale(unit_price, quantity)

    discount_amount, discount_rate = calc_discount(gross_sale)

    total_after_discount = gross_sale - discount_amount

    tax_amount = calc_tax(total_after_discount)

    shipping_cost = calc_shipping_cost(total_after_discount)

    total_after_discount, total_amount_paid = calc_total_cost(
        gross_sale,
        discount_amount,
        tax_amount,
        shipping_cost
    )

    print_results(
        gross_sale,
        discount_rate,
        discount_amount,
        total_after_discount,
        tax_amount,
        shipping_cost,
        total_amount_paid
    )


if __name__ == "__main__":
    main()
