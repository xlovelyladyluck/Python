"""
Program: main.py
Author: Taylor Wilkens
Last date modified: 09/13/2020



The purpose of this program is to accept 3 test scores, record a students name,
and output the average of the input test scores
"""

from format_output.average_scores import average

first_name1 = str(input("Please enter your first name."))
last_name1 = str(input("Please enter your last name."))
score1 = float(input("Please enter your first test score"))
score2 = float(input("Please enter your second test score"))
score3 = float(input("Please enter your final test score"))

average_score = average(score1, score2, score3)

print(last_name1+ ", "+first_name1+" Average test score: "+str(average_score))

### I felt more confident with this project, and I feel like the debugging is getting easier
### as I understand how the operations should work as well as what the data types need to be
### and how the functions need to interact between the file tabs.
