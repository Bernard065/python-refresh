age = int(input("What is your age? "))
has_id = True

if age >= 18:
    if has_id:
        print("You can enter the club")
    else:
        print("You need an ID to enter")
else:
    print("You are not old enough to enter")
