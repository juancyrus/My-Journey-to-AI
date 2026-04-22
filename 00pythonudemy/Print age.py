# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your name?:")
age = int(input("How old are you?: "))
current_year = __import__('datetime').date.today().year
if age == 100:
    print("You turned 100 this year")
else:
    year_turn_100 = current_year + (100 - age)
    print(f"Hi {name}! You will turn 100 years old in {year_turn_100}.")

    