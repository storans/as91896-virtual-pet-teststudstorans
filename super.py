# Check if person is eligible for superannuation

# Age is a constant because it's not changed in the program
SUPER_AGE = 65

# Loop to allow testing of different values
keep_going = ""
while keep_going == "":
    age = int(input("How old are you?"))

    # Must be greater than OR equal to catch 65 year olds
    if age >= SUPER_AGE:
        print("You are eligible for Govt super.")
    else:
        print("Not eligible for Govt super yet.")

    keep_going = input("Continue? <enter> or q")
