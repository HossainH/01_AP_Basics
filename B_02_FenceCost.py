
# Function to check that number entered is more than zero
def num_check(prompt):
    error = "Please enter a number that is more than zero"

    while True:
        try:
            # Ask for a number with the custom prompt
            response = float(input(prompt))

            # Check if the number is valid
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print("Please enter numbers only")

# Main routine
keep_going = ""

while keep_going == "":
    # Get width and height separately using the number checker
    width = num_check("Enter Width: ")
    length = num_check("Enter Length: ")

    print(f"Width is {width}")
    print(f"Length is {length}")

    while True:
        try:
            CostOfFencing = float(input("Enter cost of fencing per meter: "))
            if CostOfFencing == 0:
                print("Lucky you! getting it done for free I see!")
                break
            elif CostOfFencing < 0:
                print("Please enter a valid cost")
            else:
                break
        except ValueError:
            print("Please enter a number")



    perimeter = 2 * (width + length)

    print(f"the perimeter is {perimeter} meters")

    costoffencing = perimeter * CostOfFencing

    print(f"The cost of fencing your area is {costoffencing}")

    keep_going = input("Press enter key to use again, or press any key, then enter to stop")


print("Thank you for using the calculator")





