first_name1 = str(input("Please enter your first name."))
last_name1 = str(input("Please enter your last name."))
try:
    score1 = float(input("Please enter your first test score"))
    assert score1 > 0
except AssertionError:
    print("Please enter a non-negative value.")
try:
    score2 = float(input("Please enter your second test score"))
    assert score2 > 0
except AssertionError:
    print("Please enter a non-negative value.")
try:
    score3 = float(input("Please enter your final test score"))
    assert score3 > 0
except AssertionError:
    print("Please enter a non-negative value.")

def average(x, y, z):
    total = x + y + z
    the_average = total / 3
    return the_average


average_score = average(score1, score2, score3)


print(last_name1 + ", " + first_name1 + " Average test score: " + str(average_score))
