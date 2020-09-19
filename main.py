subscription_type = str(input("Please choose a membership level from the following: Platinum, Gold, Silver, Bronze or Free Trial."))

if subscription_type == "platinum":
    print("You have chosen the Platinum membership. Your monthly fee is $60.")
elif subscription_type == "gold":
    print("You have chosen the Gold membership. Your monthly fee is $50.")
elif subscription_type == "silver":
    print("You have chosen the Silver membership. Your monthly fee is $40.")
elif subscription_type == "bronze":
    print("You have chosen the Bronze membership. Your monthly fee is $30.")
elif subscription_type == "free trial":
    print("You have chosen the Free Trial membership. There is no monthly fee.")
else:
    print("Your answer is invalid.")
