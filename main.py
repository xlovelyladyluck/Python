"""
Program: camper_age_input.py
Author: Taylor Wilkens
Last date modified: 09/07/2020



The purpose of this program is to accept user input for infant camper age,
convert to the age in months to years via a function call then print the
result.
"""
from Main import camper_age_input
from Main.camper_age_input import convert_to_months

value = int(input("Please provide the infant's age."))
age_in_years = float(value)
MONTHS = 12
result = convert_to_months(age_in_years, MONTHS)

print(str(age_in_years)+" years is "+str(result)+" months old.")

#I expected this program to run as a normal, but there is something wrong with the logic and the testing will not
#connect to my function I am writing. The program does run and accept input, but the function's logic is not correct.
