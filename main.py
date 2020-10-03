def hourly_employee_input():
    """"Prompts the user for their name, hours worked, and rate of pay per hour. Prints the user input."""
    employee_name = input("Enter your name.")
    try:
        hours_worked = int(input("Enter hours worked."))
    except ValueError as err:
        print("Please input a whole number.")
        hours_worked = int(input("Enter hours worked."))
    try:
        pay_rate = float(input("Enter rate of pay per hour."))
    except ValueError as err:
        print("Please input a float only.")
        pay_rate = float(input("Enter rate of pay per hour."))

    print(employee_name, " worked ", hours_worked, " for ", pay_rate, " dollars per hour.")


if __name__ == '__main__':
    try:
        hourly_employee_input()
    except ValueError as err:
        print("ValueError encountered.")
