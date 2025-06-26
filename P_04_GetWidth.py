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

width = num_check("Enter width: ")
height = num_check("Enter height: ")

print(f"the entered width is {width}")
print(f"the entered height is {height}")
