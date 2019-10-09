SUPER_AGE = 65

keep_going = ""
while keep_going == "":
    age = int(input("How old are you?"))

    if age >= SUPER_AGE:
        print("You are eligible for Govt super.")
    else:
        print("Not eligible for Govt super yet.")

    keep_going = input("Continue? <enter> or q")
