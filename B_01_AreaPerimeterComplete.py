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
    width = num_check("Enter width: ")
    height = num_check("Enter height: ")

    print(f"Width is {width}")
    print(f"Height is {height}")

    area = width * height
    perimeter = 2 * (width + height)

    print(f"The area is {area} units")
    print(f"The perimeter is {perimeter} units")

    keep_going = input("Press Enter to use again, or type any key then Enter to stop: ")

print("Thanks for using our simple program!")



