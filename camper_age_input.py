"""
Program: camper_age_input.py
Author: Taylor Wilkens
Last date modified: 09/07/2020



The purpose of this program is to accept user input for infant camper age,
convert to the age in months to years via a function call then print the
result.
"""


def convert_to_months(years, months):

    age_in_months = 12 * years / months
    return float(age_in_months)


if __name__ == '__main__':
    convert_to_months()
