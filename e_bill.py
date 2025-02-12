import os

MAX_NAME = 50


def calculate_bill(units):
    if units < 500:
        charge = units * 1.00
    elif units < 600:
        charge = (500 * 1.00) + ((units - 500) * 1.80)
    elif units < 800:
        charge = (500 * 1.00) + (100 * 1.80) + ((units - 600) * 2.00)
    else:
        charge = (500 * 1.00) + (100 * 1.80) + (200 * 2.00) + ((units - 800) * 3.00)
    return charge


def print_bill(customer_id, customer_name, units, charge):
    print("\n====================================")
    print("         ELECTRICITY BILL            ")
    print("====================================\n")
    print(f"Customer ID   : {customer_id}")
    print(f"Customer Name : {customer_name}")
    print(f"Units        : {units:.2f}")
    print(f"Total Amount : ${charge:.2f}")
    print("\nThank you!")
    print("====================================")


def main():
    while True:
        # Clear the screen (works on both Windows and Unix-like systems)
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\nELECTRICITY BILLING SYSTEM")
        print("====================================\n")

        # Get customer details
        customer_id = input("Enter Customer ID: ")
        customer_name = input("Enter Customer Name: ")

        while True:
            try:
                units = float(input("Enter Units Consumed: "))
                break
            except ValueError:
                print("Please enter a valid number for units.")

        # Calculate bill
        charge = calculate_bill(units)

        # Print bill
        print_bill(customer_id, customer_name, units, charge)

        choice = input("\nDo you want to calculate another bill? (y/n): ").lower()
        if choice != 'y':
            break

    print("\nThank you for using the Electricity Billing System!")


if __name__ == "__main__":
    main()