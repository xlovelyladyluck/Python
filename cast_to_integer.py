"""
Program: cast_to_integer.py
Author: Taylor Wilkens
Last date modified:09/03/2020



The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""
value = input("Please enter something ")
new_value = int(value)
print("Your new value is ", end="")
print(new_value)
#I had a hard time discovering how to change user input into just int in one program.
#It errored out every time I put in a float or string, and I know how to convert int to string and back
#But I was unsure how to make that happen in one small program.
