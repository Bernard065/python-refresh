# Logical operator like and, or & not can be used to combine multiple conditions

age = int(input("What is your age? "))
has_id = True

if age >=18 and has_id:
    print("You can enter the club.")
else:
    print('You cannot enter the club.')